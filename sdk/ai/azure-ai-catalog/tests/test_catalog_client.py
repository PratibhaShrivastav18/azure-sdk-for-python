# ---------------------------------------------------------------------------
# test_catalog_client.py — end-to-end verification of azure-ai-catalog SDK
# Run:  python tests/test_catalog_client.py
# ---------------------------------------------------------------------------
"""
Verifies the behaviour described in the design doc:

1. CatalogClient can be created anonymously (no credential).
2. list_models() hits the live catalog API and returns ModelSummary objects.
3. Filters, ordering, and page_size are respected.
4. ModelSummary fields (name, version, publisher, registry_name,
   azure_offers, asset_id, inference_tasks, popularity) are populated.
5. The convenience CatalogClient.list_models() delegates correctly.
6. Async client mirrors the sync surface.
"""

from __future__ import annotations

import asyncio
import sys
import traceback


# ── helpers ──────────────────────────────────────────────────────────────────
_passed = 0
_failed = 0


def _check(label: str, condition: bool, detail: str = ""):
    global _passed, _failed
    if condition:
        _passed += 1
        print(f"  ✅  {label}")
    else:
        _failed += 1
        print(f"  ❌  {label}  — {detail}")


# ── Test 1: anonymous instantiation ─────────────────────────────────────────
def test_anonymous_instantiation():
    print("\n── Test 1: Anonymous instantiation ──")
    from azure.ai.catalog import CatalogClient

    client = CatalogClient()
    _check("CatalogClient() created without credential", client is not None)
    _check(
        "Default base_url is catalog endpoint",
        client._config.base_url == "https://api.catalog.azureml.ms",
        f"got {client._config.base_url}",
    )
    _check(
        "No authentication_policy set",
        client._config.authentication_policy is None,
    )
    client.close()


# ── Test 2: custom base_url ─────────────────────────────────────────────────
def test_custom_base_url():
    print("\n── Test 2: Custom base_url ──")
    from azure.ai.catalog import CatalogClient

    client = CatalogClient(base_url="https://custom.endpoint.example")
    _check(
        "base_url overridden",
        client._config.base_url == "https://custom.endpoint.example",
        f"got {client._config.base_url}",
    )
    client.close()


# ── Test 3: live list_models with filters ────────────────────────────────────
def test_list_models_live():
    print("\n── Test 3: Live list_models (filters + order + page_size) ──")
    from azure.ai.catalog import CatalogClient

    client = CatalogClient()
    results = client.list_models(
        filters=[
            {"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]},
            {"field": "labels", "operator": "eq", "values": ["latest"]},
        ],
        order_by="popularity",
        page_size=5,
    )

    _check("Result is a list", isinstance(results, list), f"type={type(results)}")
    _check("At least 1 result returned", len(results) >= 1, f"len={len(results)}")
    _check("At most page_size results", len(results) <= 5, f"len={len(results)}")

    # Every entry should be a ModelSummary
    from azure.ai.catalog.models import ModelSummary

    for i, m in enumerate(results):
        _check(f"  results[{i}] is ModelSummary", isinstance(m, ModelSummary), f"type={type(m)}")

    # First result should have the expected fields populated
    if results:
        m = results[0]
        _check("name populated", m.name is not None and len(m.name) > 0, f"name={m.name}")
        _check("version populated", m.version is not None, f"version={m.version}")
        _check("publisher populated", m.publisher is not None, f"publisher={m.publisher}")
        _check("registry_name populated", m.registry_name is not None, f"registry_name={m.registry_name}")
        _check("asset_id populated", m.asset_id is not None and m.asset_id.startswith("azureml://"), f"asset_id={m.asset_id}")
        _check("inference_tasks is list", isinstance(m.inference_tasks, list), f"type={type(m.inference_tasks)}")
        _check("popularity is float", isinstance(m.popularity, (int, float)), f"type={type(m.popularity)}")
        # azure_offers can be None (e.g. Fireworks) or a list
        _check("azure_offers is None or list", m.azure_offers is None or isinstance(m.azure_offers, list))

    # Verify name filter worked — catalog does substring matching, so every
    # result should at least contain the key tokens from the filter.
    for m in results:
        lower = (m.name or "").lower()
        _check(
            f"  '{m.name}' contains key tokens",
            "gpt" in lower and "oss" in lower and "120b" in lower,
            f"name={m.name}",
        )

    client.close()


# ── Test 4: convenience method delegates to models.list ──────────────────────
def test_convenience_delegates():
    print("\n── Test 4: CatalogClient.list_models delegates to models.list ──")
    from azure.ai.catalog import CatalogClient

    client = CatalogClient()

    direct = client.models.list(
        filters=[{"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]}],
        page_size=2,
    )
    convenience = client.list_models(
        filters=[{"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]}],
        page_size=2,
    )

    _check("Both return same count", len(direct) == len(convenience), f"{len(direct)} vs {len(convenience)}")
    if direct and convenience:
        _check(
            "First result name matches",
            direct[0].name == convenience[0].name,
            f"{direct[0].name} vs {convenience[0].name}",
        )
    client.close()


# ── Test 5: models module exports ────────────────────────────────────────────
def test_model_exports():
    print("\n── Test 5: Models module exports ──")
    from azure.ai.catalog import models

    for name in ["ModelSummary", "ModelFilter", "ModelOrder", "ModelSearchRequest",
                 "ModelSearchResponse", "FilterOperator", "OrderDirection"]:
        _check(f"{name} exported", hasattr(models, name), f"missing from azure.ai.catalog.models")


# ── Test 6: async client ────────────────────────────────────────────────────
def test_async_client():
    print("\n── Test 6: Async CatalogClient ──")
    try:
        import aiohttp  # noqa: F401
    except ImportError:
        print("  ⏭️   Skipped — aiohttp not installed")
        return
    from azure.ai.catalog.aio import CatalogClient as AsyncCatalogClient

    async def _run():
        client = AsyncCatalogClient()
        _check("Async client created", client is not None)
        results = await client.models.list(
            filters=[{"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]}],
            page_size=3,
        )
        _check("Async list returns list", isinstance(results, list))
        _check("Async list has results", len(results) >= 1, f"len={len(results)}")

        from azure.ai.catalog.models import ModelSummary
        if results:
            _check("Async result is ModelSummary", isinstance(results[0], ModelSummary))
        await client.close()

    asyncio.run(_run())


# ── Test 7: context manager ─────────────────────────────────────────────────
def test_context_manager():
    print("\n── Test 7: Context manager (sync) ──")
    from azure.ai.catalog import CatalogClient

    with CatalogClient() as client:
        results = client.list_models(
            filters=[{"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]}],
            page_size=1,
        )
        _check("Works inside 'with' block", len(results) >= 1)


# ── runner ───────────────────────────────────────────────────────────────────
def main():
    tests = [
        test_anonymous_instantiation,
        test_custom_base_url,
        test_list_models_live,
        test_convenience_delegates,
        test_model_exports,
        test_async_client,
        test_context_manager,
    ]
    for t in tests:
        try:
            t()
        except Exception:
            global _failed
            _failed += 1
            print(f"  💥  {t.__name__} raised an exception:")
            traceback.print_exc()

    print(f"\n{'='*50}")
    print(f"  {_passed} passed, {_failed} failed")
    print(f"{'='*50}")
    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()

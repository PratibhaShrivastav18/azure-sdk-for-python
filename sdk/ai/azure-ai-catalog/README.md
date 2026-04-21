# Azure AI Catalog client library for Python

The Azure AI Catalog client library allows you to discover and search AI models available in the Azure AI model catalog.

## Getting started

### Install the package

```bash
pip install azure-ai-catalog
```

### Prerequisites

- Python 3.9 or later.
- No authentication is required — the catalog API is publicly accessible.

## Key concepts

- **CatalogClient**: The main client for interacting with the Azure AI model catalog.
- **ModelSummary**: Represents a model entry returned from a catalog search.

## Examples

### Search for models by name

```python
from azure.ai.catalog import CatalogClient

catalog = CatalogClient()  # anonymous — no credential needed

models = catalog.list_models(
    filters=[
        {"field": "name", "operator": "contains", "values": ["gpt-oss-120b"]},
        {"field": "labels", "operator": "eq", "values": ["latest"]},
    ],
    order_by="popularity",
    page_size=5,
)
for model in models:
    print(f"{model.name}  v{model.version}  publisher={model.publisher}")
```

## Troubleshooting

Enable logging with `logging` module to see HTTP requests/responses.

## Next steps

See the [samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-catalog/samples) directory.

## Contributing

This project welcomes contributions. See [CONTRIBUTING.md](https://github.com/Azure/azure-sdk-for-python/blob/main/CONTRIBUTING.md).

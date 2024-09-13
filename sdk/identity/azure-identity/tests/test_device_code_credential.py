# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import datetime
from unittest.mock import ANY, Mock, patch

from azure.core.exceptions import ClientAuthenticationError
from azure.core.pipeline.policies import SansIOHTTPPolicy
from azure.identity import AuthenticationRequiredError, DeviceCodeCredential
from azure.identity._internal.user_agent import USER_AGENT
import pytest

from helpers import (
    build_aad_response,
    build_id_token,
    get_discovery_response,
    id_token_claims,
    mock_response,
    Request,
    validating_transport,
)


def test_tenant_id_validation():
    """The credential should raise ValueError when given an invalid tenant_id"""

    valid_ids = {"c878a2ab-8ef4-413b-83a0-199afb84d7fb", "contoso.onmicrosoft.com", "organizations", "common"}
    for tenant in valid_ids:
        DeviceCodeCredential(tenant_id=tenant)

    invalid_ids = {"my tenant", "my_tenant", "/", "\\", '"my-tenant"', "'my-tenant'"}
    for tenant in invalid_ids:
        with pytest.raises(ValueError):
            DeviceCodeCredential(tenant_id=tenant)


def test_no_scopes():
    """The credential should raise when get_token is called with no scopes"""

    credential = DeviceCodeCredential("client_id")
    with pytest.raises(ValueError):
        credential.get_token()


def test_authenticate():
    client_id = "client-id"
    environment = "localhost"
    issuer = "https://" + environment
    tenant_id = "some-tenant"
    authority = issuer + "/" + tenant_id

    access_token = "***"
    scope = "scope"

    # mock Microsoft Entra ID response with id token
    object_id = "object-id"
    home_tenant = "home-tenant-id"
    username = "me@work.com"
    id_token = build_id_token(aud=client_id, iss=issuer, object_id=object_id, tenant_id=home_tenant, username=username)
    auth_response = build_aad_response(
        uid=object_id, utid=home_tenant, access_token=access_token, refresh_token="**", id_token=id_token
    )

    transport = validating_transport(
        requests=[Request(url_substring=issuer)] * 4,
        responses=[get_discovery_response(authority)] * 2  # instance and tenant discovery
        + [
            mock_response(  # start device code flow
                json_payload={
                    "device_code": "_",
                    "user_code": "user-code",
                    "verification_uri": "verification-uri",
                    "expires_in": 42,
                }
            ),
            mock_response(json_payload=dict(auth_response, scope=scope)),  # poll for completion
        ],
    )

    credential = DeviceCodeCredential(
        client_id,
        prompt_callback=Mock(),  # prevent credential from printing to stdout
        transport=transport,
        authority=environment,
        tenant_id=tenant_id,
    )
    record = credential.authenticate(scopes=(scope,))
    assert record.authority == environment
    assert record.home_account_id == object_id + "." + home_tenant
    assert record.tenant_id == home_tenant
    assert record.username == username

    # credential should have a cached access token for the scope used in authenticate
    token = credential.get_token(scope)
    assert token.token == access_token


def test_disable_automatic_authentication():
    """When configured for strict silent auth, the credential should raise when silent auth fails"""

    transport = Mock(send=Mock(side_effect=Exception("no request should be sent")))
    credential = DeviceCodeCredential("client-id", disable_automatic_authentication=True, transport=transport)

    with pytest.raises(AuthenticationRequiredError):
        credential.get_token("scope")


def test_policies_configurable():
    policy = Mock(spec_set=SansIOHTTPPolicy, on_request=Mock())

    client_id = "client-id"
    transport = validating_transport(
        requests=[Request()] * 3,
        responses=[
            # expected requests: discover tenant, start device code flow, poll for completion
            get_discovery_response(),
            mock_response(
                json_payload={
                    "device_code": "_",
                    "user_code": "user-code",
                    "verification_uri": "verification-uri",
                    "expires_in": 42,
                }
            ),
            mock_response(
                json_payload=dict(
                    build_aad_response(access_token="**", id_token=build_id_token(aud=client_id)), scope="scope"
                )
            ),
        ],
    )

    credential = DeviceCodeCredential(
        client_id=client_id, prompt_callback=Mock(), policies=[policy], transport=transport
    )

    credential.get_token("scope")

    assert policy.on_request.called


def test_user_agent():
    client_id = "client-id"
    transport = validating_transport(
        requests=[Request()] * 2 + [Request(required_headers={"User-Agent": USER_AGENT})],
        responses=[
            get_discovery_response(),
            mock_response(
                json_payload={
                    "device_code": "_",
                    "user_code": "user-code",
                    "verification_uri": "verification-uri",
                    "expires_in": 42,
                }
            ),
            mock_response(
                json_payload=dict(
                    build_aad_response(access_token="**", id_token=build_id_token(aud=client_id)), scope="scope"
                )
            ),
        ],
    )

    credential = DeviceCodeCredential(client_id=client_id, prompt_callback=Mock(), transport=transport)

    credential.get_token("scope")


def test_device_code_credential():
    client_id = "client-id"
    expected_token = "access-token"
    user_code = "user-code"
    verification_uri = "verification-uri"
    expires_in = 42

    transport = validating_transport(
        requests=[Request()] * 3,  # not validating requests because they're formed by MSAL
        responses=[
            # expected requests: discover tenant, start device code flow, poll for completion
            get_discovery_response(),
            mock_response(
                json_payload={
                    "device_code": "_",
                    "user_code": user_code,
                    "verification_uri": verification_uri,
                    "expires_in": expires_in,
                }
            ),
            mock_response(
                json_payload=dict(
                    build_aad_response(
                        access_token=expected_token,
                        expires_in=expires_in,
                        refresh_token="_",
                        id_token=build_id_token(aud=client_id),
                    ),
                    scope="scope",
                ),
            ),
        ],
    )

    callback = Mock()
    credential = DeviceCodeCredential(
        client_id=client_id,
        prompt_callback=callback,
        transport=transport,
        disable_instance_discovery=True,
    )

    now = datetime.datetime.now(datetime.timezone.utc)
    token = credential.get_token("scope")
    assert token.token == expected_token

    # prompt_callback should have been called as documented
    assert callback.call_count == 1
    uri, code, expires_on = callback.call_args[0]
    assert uri == verification_uri
    assert code == user_code

    # validating expires_on exactly would require depending on internals of the credential and
    # patching time, so we'll be satisfied if expires_on is a datetime at least expires_in
    # seconds later than our call to get_token
    assert isinstance(expires_on, datetime.datetime)
    assert expires_on - now >= datetime.timedelta(seconds=expires_in)


def test_tenant_id():
    client_id = "client-id"
    expected_token = "access-token"
    user_code = "user-code"
    verification_uri = "verification-uri"
    expires_in = 42

    transport = validating_transport(
        requests=[Request()] * 3,  # not validating requests because they're formed by MSAL
        responses=[
            # expected requests: discover tenant, start device code flow, poll for completion
            get_discovery_response(),
            mock_response(
                json_payload={
                    "device_code": "_",
                    "user_code": user_code,
                    "verification_uri": verification_uri,
                    "expires_in": expires_in,
                }
            ),
            mock_response(
                json_payload=dict(
                    build_aad_response(
                        access_token=expected_token,
                        expires_in=expires_in,
                        refresh_token="_",
                        id_token=build_id_token(aud=client_id),
                    ),
                    scope="scope",
                ),
            ),
        ],
    )

    callback = Mock()
    credential = DeviceCodeCredential(
        client_id=client_id,
        prompt_callback=callback,
        transport=transport,
        disable_instance_discovery=True,
        additionally_allowed_tenants=["*"],
    )

    token = credential.get_token("scope", tenant_id="tenant_id")
    assert token.token == expected_token


def test_timeout():
    flow = {"expires_in": 1800, "message": "foo"}
    with patch.object(DeviceCodeCredential, "_get_app") as get_app:
        msal_app = get_app()
        msal_app.initiate_device_flow.return_value = flow
        msal_app.acquire_token_by_device_flow.return_value = {"error": "authorization_pending"}

        credential = DeviceCodeCredential(client_id="_", timeout=1, disable_instance_discovery=True)
        with pytest.raises(ClientAuthenticationError) as ex:
            credential.get_token("scope")
        assert "timed out" in ex.value.message.lower()
        msal_app.acquire_token_by_device_flow.assert_called_once_with(flow, exit_condition=ANY, claims_challenge=None)


def test_client_capabilities():
    """the credential should configure MSAL for capability CP1 only if enable_cae is passed."""

    transport = Mock(send=Mock(side_effect=Exception("this test mocks MSAL, so no request should be sent")))
    credential = DeviceCodeCredential(transport=transport)
    with patch("msal.PublicClientApplication") as PublicClientApplication:
        credential._get_app()

        assert PublicClientApplication.call_count == 1
        _, kwargs = PublicClientApplication.call_args
        assert kwargs["client_capabilities"] == None

        credential._get_app(enable_cae=True)

        assert PublicClientApplication.call_count == 2
        _, kwargs = PublicClientApplication.call_args
        assert kwargs["client_capabilities"] == ["CP1"]


def test_claims_challenge():
    """get_token and authenticate should pass any claims challenge to MSAL token acquisition APIs"""

    msal_acquire_token_result = dict(
        build_aad_response(access_token="**", id_token=build_id_token()),
        id_token_claims=id_token_claims("issuer", "subject", "audience", upn="upn"),
    )
    expected_claims = '{"access_token": {"essential": "true"}'

    transport = Mock(send=Mock(side_effect=Exception("this test mocks MSAL, so no request should be sent")))
    credential = DeviceCodeCredential(transport=transport)
    with patch.object(DeviceCodeCredential, "_get_app") as get_mock_app:
        msal_app = get_mock_app()
        msal_app.initiate_device_flow.return_value = {"message": "it worked"}
        msal_app.acquire_token_by_device_flow.return_value = msal_acquire_token_result

        credential.authenticate(scopes=["scope"], claims=expected_claims)

        assert msal_app.acquire_token_by_device_flow.call_count == 1
        args, kwargs = msal_app.acquire_token_by_device_flow.call_args
        assert kwargs["claims_challenge"] == expected_claims

        credential.get_token("scope", claims=expected_claims)

        assert msal_app.acquire_token_by_device_flow.call_count == 2
        args, kwargs = msal_app.acquire_token_by_device_flow.call_args
        assert kwargs["claims_challenge"] == expected_claims

        msal_app.get_accounts.return_value = [{"home_account_id": credential._auth_record.home_account_id}]
        msal_app.acquire_token_silent_with_error.return_value = msal_acquire_token_result
        credential.get_token("scope", claims=expected_claims)

        assert msal_app.acquire_token_silent_with_error.call_count == 1
        args, kwargs = msal_app.acquire_token_silent_with_error.call_args
        assert kwargs["claims_challenge"] == expected_claims

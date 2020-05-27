# Stubs for azure.storage.blob._shared.authentication (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from azure.core.exceptions import ClientAuthenticationError
from azure.core.pipeline.policies import SansIOHTTPPolicy
from typing import Any

logger: Any

class AzureSigningError(ClientAuthenticationError): ...

class SharedKeyCredentialPolicy(SansIOHTTPPolicy):
    account_name: Any = ...
    account_key: Any = ...
    def __init__(self, account_name: Any, account_key: Any) -> None: ...
    def on_request(self, request: Any) -> None: ...

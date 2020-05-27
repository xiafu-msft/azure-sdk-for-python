# Stubs for azure.storage.blob._lease (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._generated.models import LeaseAccessConditions, StorageErrorException
from ._generated.operations import BlobOperations, ContainerOperations
from ._serialize import get_modify_conditions
from ._shared.response_handlers import process_storage_error, return_response_headers
from typing import Any, Optional, TypeVar, Union

BlobClient = TypeVar('BlobClient')
ContainerClient = TypeVar('ContainerClient')

def get_access_conditions(lease: Optional[Union[BlobLeaseClient, str]]) -> Union[LeaseAccessConditions, None]: ...

class BlobLeaseClient:
    id: Any = ...
    last_modified: Any = ...
    etag: Any = ...
    def __init__(self, client: Union[BlobClient, ContainerClient], lease_id: Optional[str]=...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args: Any) -> None: ...
    def acquire(self, lease_duration: int=..., **kwargs: Any) -> None: ...
    def renew(self, **kwargs: Any) -> None: ...
    def release(self, **kwargs: Any) -> None: ...
    def change(self, proposed_lease_id: str, **kwargs: Any) -> None: ...
    def break_lease(self, lease_break_period: Optional[int]=..., **kwargs: Any) -> int: ...

# Stubs for azure.storage.fileshare.aio._models (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .._generated.models import DirectoryItem, StorageErrorException
from .._models import Handle, ShareProperties
from .._shared.response_handlers import process_storage_error, return_context_and_deserialized
from azure.core.async_paging import AsyncPageIterator
from typing import Any, Optional

class SharePropertiesPaged(AsyncPageIterator):
    service_endpoint: Any = ...
    prefix: Any = ...
    marker: Any = ...
    results_per_page: Any = ...
    location_mode: Any = ...
    current_page: Any = ...
    def __init__(self, command: Any, prefix: Optional[Any] = ..., results_per_page: Optional[Any] = ..., continuation_token: Optional[Any] = ...) -> None: ...

class HandlesPaged(AsyncPageIterator):
    marker: Any = ...
    results_per_page: Any = ...
    location_mode: Any = ...
    current_page: Any = ...
    def __init__(self, command: Any, results_per_page: Optional[Any] = ..., continuation_token: Optional[Any] = ...) -> None: ...

class DirectoryPropertiesPaged(AsyncPageIterator):
    service_endpoint: Any = ...
    prefix: Any = ...
    marker: Any = ...
    results_per_page: Any = ...
    location_mode: Any = ...
    current_page: Any = ...
    def __init__(self, command: Any, prefix: Optional[Any] = ..., results_per_page: Optional[Any] = ..., continuation_token: Optional[Any] = ...) -> None: ...

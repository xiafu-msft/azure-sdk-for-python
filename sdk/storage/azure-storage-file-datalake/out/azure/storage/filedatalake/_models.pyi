# Stubs for azure.storage.filedatalake._models (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._deserialize import return_headers_and_deserialized_path_list
from ._generated.models import Path
from ._shared.models import DictMixin
from ._shared.response_handlers import process_storage_error
from azure.core.paging import PageIterator
from azure.storage.blob import AccessPolicy as BlobAccessPolicy, AccountSasPermissions as BlobAccountSasPermissions, BlobSasPermissions, ContainerSasPermissions, ContentSettings as BlobContentSettings, LeaseProperties as BlobLeaseProperties, ResourceTypes as BlobResourceTypes, UserDelegationKey as BlobUserDelegationKey
from azure.storage.blob._models import ContainerPropertiesPaged
from enum import Enum
from typing import Any, Optional

class FileSystemProperties:
    name: Any = ...
    last_modified: Any = ...
    etag: Any = ...
    lease: Any = ...
    public_access: Any = ...
    has_immutability_policy: Any = ...
    has_legal_hold: Any = ...
    metadata: Any = ...
    def __init__(self) -> None: ...

class FileSystemPropertiesPaged(ContainerPropertiesPaged):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class DirectoryProperties(DictMixin):
    name: Any = ...
    etag: Any = ...
    deleted: Any = ...
    metadata: Any = ...
    lease: Any = ...
    last_modified: Any = ...
    creation_time: Any = ...
    deleted_time: Any = ...
    remaining_retention_days: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...

class FileProperties(DictMixin):
    name: Any = ...
    etag: Any = ...
    deleted: Any = ...
    metadata: Any = ...
    lease: Any = ...
    last_modified: Any = ...
    creation_time: Any = ...
    size: Any = ...
    deleted_time: Any = ...
    remaining_retention_days: Any = ...
    content_settings: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...

class PathProperties:
    name: Any = ...
    owner: Any = ...
    group: Any = ...
    permissions: Any = ...
    last_modified: Any = ...
    is_directory: Any = ...
    etag: Any = ...
    content_length: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...

class PathPropertiesPaged(PageIterator):
    recursive: Any = ...
    results_per_page: Any = ...
    path: Any = ...
    upn: Any = ...
    current_page: Any = ...
    path_list: Any = ...
    def __init__(self, command: Any, recursive: Any, path: Optional[Any] = ..., max_results: Optional[Any] = ..., continuation_token: Optional[Any] = ..., upn: Optional[Any] = ...) -> None: ...

class LeaseProperties(BlobLeaseProperties):
    status: Any = ...
    state: Any = ...
    duration: Any = ...
    def __init__(self) -> None: ...

class ContentSettings(BlobContentSettings):
    def __init__(self, **kwargs: Any) -> None: ...

class AccountSasPermissions(BlobAccountSasPermissions):
    def __init__(self, read: bool = ..., write: bool = ..., delete: bool = ..., list: bool = ..., create: bool = ...) -> None: ...

class FileSystemSasPermissions(ContainerSasPermissions):
    def __init__(self, read: bool = ..., write: bool = ..., delete: bool = ..., list: bool = ...) -> None: ...

class DirectorySasPermissions(BlobSasPermissions):
    def __init__(self, read: bool = ..., create: bool = ..., write: bool = ..., delete: bool = ...) -> None: ...

class FileSasPermissions(BlobSasPermissions):
    def __init__(self, read: bool = ..., create: bool = ..., write: bool = ..., delete: bool = ...) -> None: ...

class AccessPolicy(BlobAccessPolicy):
    def __init__(self, permission: Optional[Any] = ..., expiry: Optional[Any] = ..., **kwargs: Any) -> None: ...

class ResourceTypes(BlobResourceTypes):
    def __init__(self, service: bool = ..., file_system: bool = ..., object: bool = ...) -> None: ...

class UserDelegationKey(BlobUserDelegationKey): ...

class PublicAccess(str, Enum):
    File: str = ...
    FileSystem: str = ...

class LocationMode:
    PRIMARY: str = ...
    SECONDARY: str = ...

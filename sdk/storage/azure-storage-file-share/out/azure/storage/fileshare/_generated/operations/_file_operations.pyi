# Stubs for azure.storage.fileshare._generated.operations._file_operations (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class FileOperations:
    models: Any = ...
    x_ms_type: str = ...
    x_ms_write: str = ...
    x_ms_copy_action: str = ...
    def __init__(self, client: Any, config: Any, serializer: Any, deserializer: Any) -> None: ...
    def create(self, file_content_length: Any, file_attributes: str = ..., file_creation_time: str = ..., file_last_write_time: str = ..., timeout: Optional[Any] = ..., metadata: Optional[Any] = ..., file_permission: str = ..., file_permission_key: Optional[Any] = ..., file_http_headers: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def download(self, timeout: Optional[Any] = ..., range: Optional[Any] = ..., range_get_content_md5: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def get_properties(self, sharesnapshot: Optional[Any] = ..., timeout: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def delete(self, timeout: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def set_http_headers(self, file_attributes: str = ..., file_creation_time: str = ..., file_last_write_time: str = ..., timeout: Optional[Any] = ..., file_content_length: Optional[Any] = ..., file_permission: str = ..., file_permission_key: Optional[Any] = ..., file_http_headers: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def set_metadata(self, timeout: Optional[Any] = ..., metadata: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def upload_range(self, range: Any, content_length: Any, file_range_write: str = ..., optionalbody: Optional[Any] = ..., timeout: Optional[Any] = ..., content_md5: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def upload_range_from_url(self, range: Any, copy_source: Any, content_length: Any, timeout: Optional[Any] = ..., source_range: Optional[Any] = ..., source_content_crc64: Optional[Any] = ..., source_modified_access_conditions: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def get_range_list(self, sharesnapshot: Optional[Any] = ..., timeout: Optional[Any] = ..., range: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def start_copy(self, copy_source: Any, timeout: Optional[Any] = ..., metadata: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def abort_copy(self, copy_id: Any, timeout: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def list_handles(self, marker: Optional[Any] = ..., maxresults: Optional[Any] = ..., timeout: Optional[Any] = ..., sharesnapshot: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...
    def force_close_handles(self, handle_id: Any, timeout: Optional[Any] = ..., marker: Optional[Any] = ..., sharesnapshot: Optional[Any] = ..., cls: Optional[Any] = ..., **kwargs: Any): ...

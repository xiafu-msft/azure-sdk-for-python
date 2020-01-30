# Stubs for azure.storage.fileshare._file_client (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._deserialize import deserialize_file_properties, deserialize_file_stream
from ._download import StorageStreamDownloader
from ._generated import AzureFileStorage
from ._generated.models import FileHTTPHeaders, HandleItem, StorageErrorException
from ._generated.version import VERSION
from ._models import ContentSettings, FileProperties, Handle, HandlesPaged, NTFSAttributes, ShareProperties
from ._parser import _datetime_to_str, _get_file_permission
from ._serialize import get_source_conditions
from ._shared.base_client import StorageAccountHostsMixin, parse_connection_str, parse_query
from ._shared.parser import _str
from ._shared.request_handlers import add_metadata_headers, get_length
from ._shared.response_handlers import process_storage_error, return_response_headers
from ._shared.uploads import FileChunkUploader, IterStreamer, upload_data_chunks
from azure.core.paging import ItemPaged
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Union

class ShareFileClient(StorageAccountHostsMixin):
    snapshot: Any = ...
    share_name: Any = ...
    file_path: Any = ...
    file_name: Any = ...
    directory_path: Any = ...
    def __init__(self, account_url: str, share_name: str, file_path: str, snapshot: Optional[Union[str, Dict[str, Any]]]=..., credential: Optional[Any]=..., **kwargs: Any) -> None: ...
    @classmethod
    def from_file_url(cls: Any, file_url: str, snapshot: Optional[Union[str, Dict[str, Any]]]=..., credential: Optional[Any]=..., **kwargs: Any) -> ShareFileClient: ...
    @classmethod
    def from_connection_string(cls: Any, conn_str: str, share_name: str, file_path: str, snapshot: Optional[Union[str, Dict[str, Any]]]=..., credential: Optional[Any]=..., **kwargs: Any) -> ShareFileClient: ...
    def create_file(self, size: int, file_attributes: Union[str, NTFSAttributes]=..., file_creation_time: Union[str, datetime]=..., file_last_write_time: Union[str, datetime]=..., file_permission: Optional[str]=..., permission_key: Optional[str]=..., **kwargs: Any) -> Dict[str, Any]: ...
    def upload_file(self, data: Any, length: Optional[int]=..., file_attributes: Union[str, NTFSAttributes]=..., file_creation_time: Union[str, datetime]=..., file_last_write_time: Union[str, datetime]=..., file_permission: Optional[str]=..., permission_key: Optional[str]=..., **kwargs: Any) -> Dict[str, Any]: ...
    def start_copy_from_url(self, source_url: str, **kwargs: Any) -> Any: ...
    def abort_copy(self, copy_id: Union[str, FileProperties], **kwargs: Any) -> None: ...
    def download_file(self, offset: Optional[int]=..., length: Optional[int]=..., **kwargs: Any) -> Iterable[bytes]: ...
    def delete_file(self, **kwargs: Any) -> None: ...
    def get_file_properties(self, **kwargs: Any) -> FileProperties: ...
    def set_http_headers(self, content_settings: ContentSettings, file_attributes: Union[str, NTFSAttributes]=..., file_creation_time: Union[str, datetime]=..., file_last_write_time: Union[str, datetime]=..., file_permission: Optional[str]=..., permission_key: Optional[str]=..., **kwargs: Any) -> Dict[str, Any]: ...
    def set_file_metadata(self, metadata: Optional[Dict[str, Any]]=..., **kwargs: Any) -> Dict[str, Any]: ...
    def upload_range(self, data: bytes, offset: int, length: int, **kwargs: Any) -> Dict[str, Any]: ...
    def upload_range_from_url(self, source_url: str, offset: int, length: int, source_offset: int, **kwargs: Any) -> Dict[str, Any]: ...
    def get_ranges(self, offset: Optional[int]=..., length: Optional[int]=..., **kwargs: Any) -> List[Dict[str, int]]: ...
    def clear_range(self, offset: int, length: int, **kwargs: Any) -> Dict[str, Any]: ...
    def resize_file(self, size: int, **kwargs: Any) -> Dict[str, Any]: ...
    def list_handles(self, **kwargs: Any) -> ItemPaged[Handle]: ...
    def close_handle(self, handle: Union[str, HandleItem], **kwargs: Any) -> Dict[str, int]: ...
    def close_all_handles(self, **kwargs: Any) -> Dict[str, int]: ...

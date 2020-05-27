# Stubs for azure.storage.blob._upload_helpers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._generated.models import AppendPositionAccessConditions, BlockLookupList, ModifiedAccessConditions, StorageErrorException
from ._shared.encryption import encrypt_blob, generate_blob_encryption_data
from ._shared.models import StorageErrorCode
from ._shared.response_handlers import process_storage_error, return_response_headers
from ._shared.uploads import AppendBlobChunkUploader, BlockBlobChunkUploader, PageBlobChunkUploader, upload_data_chunks, upload_substream_blocks
from typing import Any, Optional, TypeVar

BlobLeaseClient = TypeVar('BlobLeaseClient')

def upload_block_blob(client: Optional[Any] = ..., data: Optional[Any] = ..., stream: Optional[Any] = ..., length: Optional[Any] = ..., overwrite: Optional[Any] = ..., headers: Optional[Any] = ..., validate_content: Optional[Any] = ..., max_concurrency: Optional[Any] = ..., blob_settings: Optional[Any] = ..., encryption_options: Optional[Any] = ..., **kwargs: Any): ...
def upload_page_blob(client: Optional[Any] = ..., stream: Optional[Any] = ..., length: Optional[Any] = ..., overwrite: Optional[Any] = ..., headers: Optional[Any] = ..., validate_content: Optional[Any] = ..., max_concurrency: Optional[Any] = ..., blob_settings: Optional[Any] = ..., encryption_options: Optional[Any] = ..., **kwargs: Any): ...
def upload_append_blob(client: Optional[Any] = ..., stream: Optional[Any] = ..., length: Optional[Any] = ..., overwrite: Optional[Any] = ..., headers: Optional[Any] = ..., validate_content: Optional[Any] = ..., max_concurrency: Optional[Any] = ..., blob_settings: Optional[Any] = ..., encryption_options: Optional[Any] = ..., **kwargs: Any): ...

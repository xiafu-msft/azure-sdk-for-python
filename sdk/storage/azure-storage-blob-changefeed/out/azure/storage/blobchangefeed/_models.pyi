# Stubs for azure.storage.blobchangefeed._models (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from azure.core.paging import PageIterator
from typing import Any, Optional

SEGMENT_COMMON_PATH: str
PATH_DELIMITER: str

class ChangeFeedPaged(PageIterator):
    results_per_page: Any = ...
    current_page: Any = ...
    def __init__(self, container_client: Any, results_per_page: Optional[Any] = ..., start_time: Optional[Any] = ..., end_time: Optional[Any] = ..., continuation_token: Optional[Any] = ...) -> None: ...

class ChangeFeed:
    client: Any = ...
    page_size: Any = ...
    unprocessed_segment_paths: Any = ...
    current_segment: Any = ...
    start_time: Any = ...
    end_time: Any = ...
    cursor: Any = ...
    def __init__(self, client: Any, page_size: Any, start_time: Optional[Any] = ..., end_time: Optional[Any] = ..., cf_cursor: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Any = ...

class Segment:
    client: Any = ...
    segment_path: Any = ...
    page_size: Any = ...
    shards: Any = ...
    cursor: Any = ...
    def __init__(self, client: Any, segment_path: Any, page_size: Any, segment_cursor: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Any = ...

class Shard:
    client: Any = ...
    shard_path: Any = ...
    current_chunk: Any = ...
    unprocessed_chunk_path_props: Any = ...
    cursor: Any = ...
    def __init__(self, client: Any, shard_path: Any, shard_cursor: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Any = ...

class Chunk:
    client: Any = ...
    chunk_path: Any = ...
    file_reader: Any = ...
    cursor: Any = ...
    def __init__(self, client: Any, chunk_path: Any, chunk_cursor: Optional[Any] = ...) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
    next: Any = ...

class ChangeFeedStreamer:
    event_position: Any = ...
    block_count: Any = ...
    def __init__(self, blob_client: Any, chunk_file_start: int = ..., block_count: int = ...) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def seekable(self): ...
    def next(self): ...
    def tell(self): ...
    def seek(self, offset: Any, whence: int = ...) -> None: ...
    def read(self, size: Any): ...
    def track_event_position(self) -> None: ...

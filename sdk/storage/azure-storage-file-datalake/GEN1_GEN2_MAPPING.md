#
# Mapping from ADLS Gen1 API -\> ADLS Gen2 API

| ADLS Gen1 API | Note for Gen1 API | ADLS Gen2 API | Note for API Mapping |
| --- | --- | --- | --- |
| access/exists | To check if file/directory exists. | N/A | User can use Gen2 API: **create\_file(if\_non\_match=&#39;\*&#39;)**Or**create\_directory(if\_non\_match=&#39;\*&#39;)**so that the operation will fail on exist. |
| touch | Create empty file | **create\_file** | The API has the same main purpose for Gen1 and Gen2. However Gen2 **create\_file** api could accept more parameters along with creation. |
| mkdir | Make new directory | **create\_directory** | The API has the same main purpose for Gen1 and Gen2. However Gen2 **create\_directory** api could accept more parameters along with creation. |
| stat/info | File information for path  | **get\_file\_properties**   | The Gen1 api is split into two separate ones in ADLS Gen2.  |
| **get\_directory\_properties**   |
| unlink/remove/rm | Remove a file or directory | **delete\_file**   | The Gen1 api is split into two separate ones in ADLS Gen2. |
| **delete\_directory**   |
| rmdir | Remove empty directory | **delete\_directory**   | Delete directory |
| ls/listdir | List all elements under directory specified with path | **get paths** | **get\_paths(recursive=False)** is equal to **ls/listdir** |
| walk | Walk a path recursively and returns list of files and dirs(if parameter set)  | **get\_paths()** or**get\_paths(recursive=True)**is equal to **walk.**** recursive **is** True** by default. |
| put  | Stream data from local filename to file at path.  | **append\_data** together with **flush\_data** | **append\_data** should be followed by **flush\_data** , then the data is actually write into the file. **append\_data** is just to stage the data, not actually write the data into file. |
| cat | Return contents of file | **read\_file** | Put the expected range parameters in Gen2 api will achieve the same function of the 4 Gen1 APIs. |
| head | Return first bytes of file |
| tail | Return last bytes of file |
| [**read\_block**](https://docs.microsoft.com/en-us/python/api/azure-datalake-store/azure.datalake.store.core.azuredlfilesystem?view=azure-python#read-block-fn--offset--length--delimiter-none-) | Read a block of bytes from an ADL file  |
| get | Stream data from file at path to local filename | **read\_file** | Passing a **stream** parameter in **read\_file** should do the same thing as Gen1 **get** api does |
| rename/mv | Move file between locations on ADL | **Rename\_file** | Currently ADLS Gen2 only support rename.Move isn&#39;t supported yet. |
| **Rename\_directory** |
| chown | Change owner and/or owning group | **set\_access\_control** | Users can set owner, group, acl etc. using the same API. |
| chmod | Change access mode of path |
| Set\_acl | Set the Access Control List (ACL) for a file or folder.  |
| [**modify\_acl\_entries**](https://docs.microsoft.com/en-us/python/api/azure-datalake-store/azure.datalake.store.core.azuredlfilesystem?view=azure-python#modify-acl-entries-path--acl-spec--recursive-false--number-of-sub-process-none-) | Modify existing Access Control List (ACL) entries on a file or folder. If the entry does not exist it is added, otherwise it is updated based on the spec passed in. No entries are removed by this process (unlike set\_acl).  |
| get\_acl\_status | Gets Access Control List (ACL) entries for the specified file or directory. | **get\_access\_control** | The result will include owner, group, acl etc. |
| remove\_acl\_entries  | Remove existing, named, Access Control List (ACL) entries on a file or folder.If the entry does not exist already it is ignored. Default entries cannot be removed this way, please use remove\_default\_acl for that. Unnamed entries cannot be removed in this way, please use remove\_acl for that. Note: this is by default not recursive, and applies only to the file or folder specified.  | N/A | Probably users can achieve the same purpose by calling set\_access\_control with related parameters.  |
| [**remove\_acl**](https://docs.microsoft.com/en-us/python/api/azure-datalake-store/azure.datalake.store.core.azuredlfilesystem?view=azure-python#remove-acl-path-) | Remove the entire, non default, ACL from the file or folder, including unnamed entries. Default entries cannot be removed this way, please use remove\_default\_acl for that. Note: this is not recursive, and applies only to the file or folder specified. |
| remove\_default\_acl  | Remove the entire default ACL from the folder. Default entries do not exist on files, if a file is specified, this operation does nothing. Note: this is not recursive, and applies only to the folder specified.  |
| [**open**](https://docs.microsoft.com/en-us/python/api/azure-datalake-store/azure.datalake.store.core.azuredlfilesystem?view=azure-python#open-path--mode--rb---blocksize-33554432--delimiter-none-) | Open a file for reading or writing to.  | N/A | There is no open file operation In ADLS Gen2.However users can do operations to the file directly, eg. **append\_data, flush\_data, read\_file** |
| concat/merge | Concatenate a list of files into one new file | N/A | N/A |
| cp | Not implemented. Copy file between locations on ADL | N/A | N/A |
| current | Return the most recently created AzureDLFileSystem | N/A | N/A |
| df | Resource summary of path. eg. File count, directory count | N/A | get\_paths could be a helpful api. But user need to do further processing. |
| du | Bytes in keys at path | N/A | get\_paths could be a helpful api. But user need to do further processing. |
| glob | Find files (not directories) by glob-matching. | N/A | get\_paths could be a helpful api. But user need to do further processing. |
| set\_expiry  | Set or remove the expiration time on the specified file. This operation can only be executed against files.  | N/A | N/A |
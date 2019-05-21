## OOP Branch


## Running the script in pycharm without `--dev` argument
Can be done while running the client.py with arguments:
 - `-a -l` = mode all and active logging
 - `-g -l` = mode git and active logging
 - `-hg -l` = mode mercurial and active logging
 

## ExitCodes used by FIC:
- 2: File Extension not supported
- 3: The script failed to pull the dates
- 4: The -d/--days argument is not followed by an int
- 5: The provided file does not exist. Used by Function: modules.FIC_FileHandler.**file_size()**
- 6: Can't check file size for provided filename. Used by Function: modules.FIC_FileHandler.**file_size()**
- 7: Failed to rename file. Used by Function: modules.FIC_FileHandler.**rename_file_with_date()**
- 8: Access denied to read/write to provided file
- 9: No git authentication tokens found
- 10: Keyboard interrupt
- 11: Provided input is not an integer. Used in modules.FIC_MainMenu.repo_selection_menu()
- 12: Unknown repository provider.
- 301: Moved Permanently
- 302: Found
- 304: Not Modified
- 307: Temporary Redirect
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Unprocessable Entity
- 500: Internal Server Error
- 501: Not Implemented
- 503: Service Unavailable

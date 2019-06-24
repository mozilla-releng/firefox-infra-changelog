# OOP Branch

## Run modes and avaiable arugments.

Running the script can be done using:

```Bash
python3 client.py -a
```

The available arguments are shown in the following table:

| Short |    Verbose    |                       Description                             |
|  :-:  |      :-:      |                           :-:                                 |
|  -a   | --all         | Runs script for all avaiable repositories                     |
|  -g   | --git         | Runs script only for repos that are on GitHub                 |
|  -hg  | --mercurial   | Runs script only for repos that are on Mercurial              |
|  -r   | --repo        | Let the user choose for which repositories to run             |
|  -l   | --logging     | Activate logger output in the console                         |
| -days | --days        | Generate the changelog.md for _int_ amount of days            |
|  -p   | --push        | Runs for all available repositories and auto-push to github   |
| -dev  | --development | Activate development mode                                     |
|  -s   | --skip-menu   | Skip MainMenu. Used for automatization.                       |

## Running the script in pycharm without `--dev` argument

Can be done while running the client.py with arguments:

|            |                                   |
|    :-:     |              :-:                  |
|   `-a -l`  |  mode all and active logging      |
|   `-g -l`  |  mode git and active logging      |
|   `-hg -l` |  mode mercurial and active logging|

## ExitCodes used by FIC

In the following table are the predefined exitcodes that script can generate:

| Exit Code |                      Description                      |                              Used in:                              |
|:---------:|:-----------------------------------------------------:|:------------------------------------------------------------------:|
|     2     |             File Extension not supported.             |               `save()` method from FIC_FileHandler.py              |
|     4     |  The -days/--days argument is not followed by an int. |        `_set_arguments_flags()` method from FIC_MainMenu.py        |
|     5     |           The provided file does not exist.           |            `file_size()` from modules.FIC_FileHandler.py           |
|     6     |      Can't check file size for provided filename.     |        `file_size()` method from modules.FIC_FileHandler.py        |
|     7     |                 Failed to rename file.                |      `rename_file_with_date()` from modules.FIC_FileHandler.py     |
|     8     |     Access denied to read/write to provided file.     |       `is_readable()` method from modules.FIC_FileHandler.py       |
|     10    |                  Keyboard interrupt.                  |      Used in `signal_handler()` from modules.FIC_Exceptions.py     |
|     11    |           Provided input is not an integer.           |                                                                    |
|     12    |              Unknown repository provider.             |   Used in `_run_custom_repos_behavior()` from modules.FIC_Core.py  |
|     13    |                  Unknown Return Time.                 |          Used in `return_time()` from modules.Utilities.py         |
|    301    |                   Moved Permanently                   | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    302    |                         Found                         | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    304    |                      Not Modified                     | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    307    |                   Temporary Redirect                  | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    400    |                      Bad Request                      | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    401    |                      Unauthorized                     | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    403    |                       Forbidden                       | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    404    |                       Not Found                       | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    422    |                  Unprocessable Entity                 | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    500    |                 Internal Server Error                 | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    501    |                    Not Implemented                    | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |
|    503    |                  Service Unavailable                  | Defined in `handle_git_exception()` from modules.FIC_Exceptions.py |

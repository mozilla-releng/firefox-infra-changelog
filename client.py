# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import signal
from github import GithubException
from modules.FIC_Exceptions import FICExceptions
from modules.FIC_MainMenu import FICMainMenu

if __name__ == "__main__":
    exception = FICExceptions()
    signal.signal(signal.SIGINT, exception.signal_handler)
    try:
        FICMainMenu().start()
    except GithubException as error_code:
        exception.handle_git_exception(error_code.status)



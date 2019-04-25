# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_Github import FICGithub


class FICExceptions(FICGithub):
    def __init__(self):
        self.SIGINT = False
        FICGithub.__init__(self)

    def signal_handler(self, signal, frame):
        self.LOGGER.info("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
        self.SIGINT = True
        self.revert_modified_files()
        exit(10)

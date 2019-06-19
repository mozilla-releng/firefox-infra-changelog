# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_Github import FICGithub


class FICExceptions(FICGithub):
    """
    This class handle all the exceptions and interruptions that could be encountered.
    """
    def __init__(self):
        self.SIGINT = False
        FICGithub.__init__(self)
        self.e = None

    def signal_handler(self, signal, frame):
        """
        This method catch the keyboard interruption ( Ctrl + C )
        :param signal:
        :param frame:
        :return:
        """
        self.LOGGER.info("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
        self.SIGINT = True
        self.revert_modified_files()
        exit(10)

    def handle_git_exception(self, error):
        """
        This method handle the GitHub error codes that can be encountered.
        :param error:
        :return:
        """
        self.e = error
        if self.e == 301:
            self.LOGGER.critical("Error code 301: Moved Permanently")
            exit(301)

        elif self.e == 302:
            self.LOGGER.critical("Error code 302: Found")
            exit(302)

        elif self.e == 304:
            self.LOGGER.critical("Error code 304: Not Modified")
            exit(304)

        elif self.e == 307:
            self.LOGGER.critical("Error code 307: Temporary Redirect")
            exit(307)

        elif self.e == 400:
            self.LOGGER.critical("Error code 400: Bad Request error")
            exit(400)

        elif self.e == 401:
            self.LOGGER.critical("Error code 401: Unauthorized error")
            exit(401)

        elif self.e == 403:
            self.LOGGER.critical("Error code 403: Forbidden error")
            exit(403)

        elif self.e == 404:
            self.LOGGER.critical("Error code 404: Not Found")
            exit(404)

        elif self.e == 422:
            self.LOGGER.critical("Error code 422: Unprocessable Entity")
            exit(422)

        elif self.e == 500:
            self.LOGGER.critical("Error code 500: Internal Server Error")
            exit(500)

        elif self.e == 501:
            self.LOGGER.critical("Error code 501: Not implemented")
            exit(501)

        elif self.e == 503:
            self.LOGGER.critical("Error code 503: Service Unavailable")

            exit(503)

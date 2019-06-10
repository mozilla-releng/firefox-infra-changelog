# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging


class FICLogger:
    """
    This class handle the logging system of the entire project.
    """
    def __init__(self):
        from modules.config import DEFAULT_LOGGING_LEVEL, LOG_FILE_PATH
        self.log_file_path = LOG_FILE_PATH
        self.user_set_level = DEFAULT_LOGGING_LEVEL
        self.level = self._return_level()
        self.LOGGER = self._basic_logger_config()

    def _return_level(self):
        """
        This method sets the level for the logging system.
        The level is manually assigned by user to DEFAULT_LOGGING_LEVEL in config.py
        :return: it returns the level of the log system
        """
        if self.user_set_level.lower() == "debug":
            self.level = logging.DEBUG
        elif self.user_set_level.lower() == "info":
            self.level = logging.INFO
        elif self.user_set_level.lower() == "warning":
            self.level = logging.WARNING
        elif self.user_set_level.lower() == "error":
            self.level = logging.ERROR
        elif self.user_set_level.lower() == "critical":
            self.level = logging.CRITICAL
        return self.level

    def _basic_logger_config(self):
        """
        This is the configuration method for the logging message format.
        :return:
        """
        self.LOGGER = logging.basicConfig(level=self.level,
                                          format="[%(asctime)s] [%(filename)s:%(funcName) s:%(lineno)d] %(levelname)s %(message)s",
                                          datefmt="%H:%M:%S",
                                          filename=self.log_file_path)
        self.LOGGER = logging.getLogger(__name__)
        return self.LOGGER

    @staticmethod
    def console_logging():
        """
        This method changes the mode of the logging system
        to print the logging messages in the terminal.
        """
        logging.getLogger().addHandler(logging.StreamHandler())

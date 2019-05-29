# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_Logger import FICLogger
from modules.FIC_DataVault import FICDataVault
from modules.config import *
import json
import os


class FICFileHandler(FICLogger, FICDataVault):
    def __init__(self):
        FICLogger.__init__(self)
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH

        self.changelog_json = CHANGELOG_JSON_PATH
        self.changelog_md = CHANGELOG_MD_PATH
        self.data_folder = CHANGELOG_REPO_PATH
        self.path_level = self._check_dev_mode()
        self._missing_files = []

    @staticmethod
    def _check_dev_mode():
        import sys
        if "-dev" in sys.argv:
            return os.path.pardir
        else:
            return os.path.curdir

    @staticmethod
    def convert_bytes(num):
        """
        :param num: Bytes of a file. Comes from file_size()
        :return: Tuple with number and kb/mb format.
        """
        for _ in ["bytes", "kb", "mb", "gb"]:
            if num > 1024.0:
                num /= 1024.0
            else:
                size = "%3.2f" % num
                return float(size), _

    def _verify_data_folder(self):
        # Check that data folder exists.
        if not os.path.exists(self.construct_path(None, CHANGELOG_REPO_PATH)):
            # Create folder data
            os.makedirs(os.path.join(self.path_level, CHANGELOG_REPO_PATH))
            # Create file __init__.py
            open(os.path.abspath(os.path.join(self.path_level, CHANGELOG_REPO_PATH, "__init__.py")), "w").close()
            self.LOGGER.warning("Folder '{}' is missing. Recreating it.".format(CHANGELOG_REPO_PATH))

    def _verify_modules_folder(self):
        # Check that modules folder exists.
        if not os.path.exists(os.path.abspath(os.path.join(self.path_level, "modules"))):
            # Create folder modules
            os.makedirs(os.path.join(self.path_level + CHANGELOG_REPO_PATH))
            # Create file __init__.py
            open(os.path.abspath(os.path.join(self.path_level, CHANGELOG_REPO_PATH, "__init__.py")), "w").close()
            self.LOGGER.warning("Folder 'modules' is missing. Recreating it.")

    def _verify_plugins_folder(self):
        # Check that plugins folder exists.
        if not os.path.exists(os.path.abspath(os.path.join(self.path_level, "plugins"))):
            # Create folder plugins
            os.makedirs(os.path.join(self.path_level + CHANGELOG_REPO_PATH))
            # Create file __init__.py
            open(os.path.abspath(os.path.join(self.path_level, CHANGELOG_REPO_PATH, "__init__.py")), "w").close()
            self.LOGGER.warning("Folder 'plugins' is missing. Recreating it.")

    def _check_repo_files(self):
        with open(self.construct_path(None, "repositories.json"), "r") as json_data:
            files_to_check = json.load(json_data)
            # Check all Github files exist for each repository.
            for key in files_to_check["Github"].keys():
                if not os.path.exists(os.path.join(self.path_level, CHANGELOG_REPO_PATH, key.lower() + ".json")):
                    self._missing_files.append((key.lower() + ".json", "git"))

                if not os.path.exists(os.path.join(self.path_level, CHANGELOG_REPO_PATH, key.lower() + ".md")):
                    self._missing_files.append((key.lower() + ".md", "git"))

            # Check all Mercurial files exist for each repository.
            for key in files_to_check["Mercurial"].keys():
                if not os.path.exists(os.path.join(self.path_level, CHANGELOG_REPO_PATH, key.lower() + ".json")):
                    self._missing_files.append((key.lower() + ".json", "hg"))
                if not os.path.exists(os.path.join(self.path_level, CHANGELOG_REPO_PATH, key.lower() + ".md")):
                    self._missing_files.append((key.lower() + ".md", "hg"))

        if self._missing_files:
            self._create_missing_repo_files()

    def _create_missing_repo_files(self):
        for file_to_create in self._missing_files:
            new_local_file = open(self.construct_path(CHANGELOG_REPO_PATH, file_to_create[0].lower()), "w")
            if file_to_create[0].endswith(".json"):
                self.save(CHANGELOG_REPO_PATH, file_to_create[0].lower(), {})
            new_local_file.close()

    def _check_module_files(self):
        self._missing_files = []
        needed_files = ["config.py", "FIC_DataVault.py", "FIC_Exceptions.py", "FIC_FileHandler.py",
                        "FIC_Github.py", "FIC_Logger.py", "FIC_MainMenu.py",
                        "FIC_Mercurial.py"]

        for file in needed_files:
            if not os.path.exists(os.path.join(self.construct_path("modules", file))):
                self._missing_files.append(file)

        if self._missing_files:
            self._download_missing_files()

    def _download_missing_files(self):
        import requests
        base_url = "https://raw.githubusercontent.com/mozilla-releng/firefox-infra-changelog/oop/modules/"
        for file in self._missing_files:
            raw_file = requests.get(base_url + file, allow_redirects=True).text
            f = open(os.path.abspath(os.path.join(self.path_level, "modules", file)), "w")
            f.write(raw_file)
            f.close()

    def construct_path(self, directory_name, file_name):
        if (directory_name is None) and (file_name is None):
            return self._check_dev_mode()

        elif directory_name is None:
            path = os.path.join(self.path_level, file_name)
            return path
        else:
            path = os.path.join(self.path_level, directory_name, file_name)
            return path

    def check_tool_integrity(self):
        """ This method will verify that every folder and file necessary for FIC to run exists."""
        # Check if common folders exist. If not create them.
        self._verify_data_folder()
        self._verify_modules_folder()
        self._verify_plugins_folder()

        # Check that repository files, in data folder, exist. If not create them.
        self._check_repo_files()

        # Check that all python files, in modules folder, exist. If not download them from github.
        self._check_module_files()

    def load(self, directory, file_name):
        return open(self.construct_path(directory, file_name))

    def save(self, directory, file_name, content):
        if file_name.endswith(".md"):
            with open(self.construct_path(directory, file_name), "a") as markdown_file:
                markdown_file.write(content)

        elif file_name.endswith(".json"):
            with open(self.construct_path(directory, file_name), "w") as json_file:
                json.dump(content, json_file, indent=2)

        else:
            print("File Extension is not supported.")
            exit(2)

    def file_size(self, directory, file_name):
        """
        This helper function will return if a file is over 1000kb or not.
        If size > 1000: Will return True
        If size < 1000: Will return False, size
        :param directory: path to the file you want to check.
        :param file_name: name for the file you want to check it's size.
        :return:
        """
        size = None
        if os.path.exists(os.path.abspath(self.construct_path(directory, file_name))):
            file_info = os.stat(self.construct_path(directory, file_name))
            size = self.convert_bytes(file_info.st_size)
        else:
            self.LOGGER.critical("File '{}' does not exist!".format(file_name))
            exit(5)

        if (size[0] < 1000) and (size[1] == "bytes") or (size[1] == "kb"):
            self.LOGGER.debug("File size is: {} {}".format(size[0], size[1]))
            return False, float(size[0])

        elif (size[1] == "mb") or (size[1] == "gb"):
            self.LOGGER.debug("File size is: {} {}".format(size[0], size[1]))
            return True

        else:
            self.LOGGER.critical("Can't check file '{}'!".format(os.path.join(directory, file_name)))
            exit(6)

    def rename_file_with_date(self, directory, file_name, date_string):
        """
        Implemented in: issue-390, revised in PR 420
        Function that is used to rename a file and add a date to the title.
        Use case:
        rename_file_with_date((os.pardir + r"\test_file.md"), "20190323")
        or rename_file_with_date("git_files/addonscript.md", "20190323")
        :param directory: directory path.
        :param file_name: name of the file to be renamed
        :param date_string: string containing the date.
        :return:
        """
        generated_name = os.path.splitext(file_name)[0] + "." + date_string + os.path.splitext(file_name)[1]
        try:
            # Rename Existing File
            os.rename(self.construct_path(directory, file_name), self.construct_path(directory, generated_name))
            self.LOGGER.debug("Renamed element '{}' into '{}'.".format(file_name, generated_name))

            # Recreate the file.
            open(self.construct_path(directory, file_name), "w").close()

        except os.error:
            self.LOGGER.critical("Failed to rename the provided file \"{}\". Maybe new filename already exists?".format(file_name))
            exit(7)

        return generated_name

    def is_readable(self, directory_name, file_name):
        # os.access() is used with two arguments, file_name and os.R_OK to check if the file can be read
        if os.access(self.construct_path(directory_name, file_name), os.R_OK):
            self.LOGGER.debug("File \"{}\" can be read.".format(self.construct_path(directory_name, file_name)))
            return True
        else:
            self.LOGGER.critical("File \"{}\" cannot be read.".format(self.construct_path(directory_name, file_name)))
            exit(8)

    def is_writable(self, directory_name, file_name):
        # Check if the path exists
        if os.path.exists(self.construct_path(directory_name, file_name)):
            # Check if the provided path contains a valid file.
            if os.path.isfile(self.construct_path(directory_name, file_name)):
                # Checks to see if the provided file can be written
                if os.access(self.construct_path(directory_name, file_name), os.W_OK):
                    self.LOGGER.info("File \"{}\" is writable!".format(self.construct_path(directory_name, file_name)))
                    return True
                else:
                    self.LOGGER.error("File \"{}\" has acccess issues and cannot be written."
                                      .format(self.construct_path(directory_name, file_name)))
                    return False
            else:
                self.LOGGER.error("File \"{}\" is a path and can't be written."
                                  .format(self.construct_path(directory_name, file_name)))
                return False
        else:
            self.LOGGER.error("Path \"{}\" does not exist!.".format(self.construct_path(directory_name, file_name)))
            return False

    def move_to_final_location(self, old_path, old_file, new_path, new_file):

        try:
            os.rename(self.construct_path(old_path, old_file), self.construct_path(new_path, new_file))
            self.LOGGER.info("Successfully moved to new path: {}".format(self.construct_path(new_path, new_file)))
        except IOError:
            self.LOGGER.critical("Path \"{}\" does not exist "
                                 .format(self.construct_path(old_path, old_file)) +
                                 "or the final location \"{}\" has not been created"
                                 .format(self.construct_path(new_path, new_file)))

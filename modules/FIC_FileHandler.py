# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_Logger import FICLogger
from modules.FIC_DataVault import FICDataVault
import os


class FICFileHandler(FICLogger, FICDataVault):
    def __init__(self):
        FICLogger.__init__(self)
        FICDataVault.__init__(self)
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH

        self.changelog_json = CHANGELOG_JSON_PATH
        self.changelog_md = CHANGELOG_MD_PATH
        self.data_folder = CHANGELOG_REPO_PATH

    def load(self, directory, file_name):
        return open("{}{}".format(directory, file_name))
        # Use .endswith(".json|.md") to check if JSON or MD

    @staticmethod
    def _construct_path(directory, file_name):
        if directory is None:
            return file_name
        else:
            path = directory + file_name
            return path

    def save(self, directory, file_name, content):
        path = self._construct_path(directory, file_name)

        if file_name.endswith(".md"):
            with open(path, "w") as markdown_file:
                markdown_file.write("## " + self.repos_container.upper() + "\n\n")
                markdown_file.write(content + "\n\n")


        elif file_name.endswith(".json"):
            import json
            with open(path, "w") as json_file:
                json.dump(content, json_file, indent=2)

        else:
            print("File Extension is not supported.")
            exit(2)

    def file_size(self, file_path):
        """
        This helper function will return if a file is over 1000kb or not.
        If size > 1000: Will return True
        If size < 1000: Will return False, size
        :param file_path: path for the file you want to check it's size.
        :return:
        """
        size = None
        if os.path.isfile(file_path):
            file_info = os.stat(file_path)
            size = self.convert_bytes(file_info.st_size)
        else:
            self.LOGGER.critical("File {} does not exist! \n Abort!".format(file_path))
            exit(5)

        if size[0] < 1000 and size[1] == "kb":
            return False, float(size[0])
        else:
            return True

    @staticmethod
    def convert_bytes(num):
        """
        :param num: Bytes of a file. Comes from file_size()
        :return: Tuple with number and kb/mb format.
        """
        for _ in ["bytes", "kb", "mb"]:
            if num > 1024.0:
                num /= 1024.0
            else:
                size = "%3.2f" % num
                return float(size), _

    def rename_element_with_date(self, directory, file_name, date_string):
        """
        Implemented in: issue-390, revised in PR 418
        Function that is used to rename a file and add a date to the title.
        Use case:
        rename_element_with_dt((os.pardir + r"\test_file.md"), "20190323")
        or
        rename_element_with_dt("git_files/addonscript.md", "20190323")
        :param logger: logger object to log the rename.
        :param file_name: name or path+name of the file to be renamed
        :param date_string:
        :return:
        """
        generated_name = str(file_name[0:-3]) + "_" + date_string + ".md"
        try:
            os.rename(file_name, generated_name)
            self.LOGGER.info("Renamed element \"{}\" into \"{}\".".format(file_name, generated_name))

        except os.error:
            self.LOGGER.error("Failed to rename the provided file \"{}\"".format(file_name))

        return generated_name

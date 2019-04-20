# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import os


class FICFileHandler:
    def __init__(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH

        self.changelog_json = CHANGELOG_JSON_PATH
        self.changelog_md = CHANGELOG_MD_PATH
        self.data_folder = CHANGELOG_REPO_PATH

    def load(self, directory, file_name):
        return open("{}{}".format(directory, file_name))
        # Use .endswith(".json|.md") to check if JSON or MD
        #pass

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
            pass
        elif file_name.endswith(".json"):
            import json
            with open(path, "w") as json_file:
                json.dump(content, json_file, indent=2)

        else:
            print("File Extension is not supported.")
            exit(2)
        pass

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

        if size[0] < 1000 and size[1] == "kb":
            return False, float(size[0])
        else:
            return True

    def convert_bytes(self, num):
        """
        :param num: Bytes of a file. Comes from file_size()
        :return: Tuple with number and kb/mb format.
        """
        for x in ["bytes", "kb", "mb"]:
            if num > 1024.0:
                num /= 1024.0
            else:
                a = "%3.2f" % num
                return float(a), x

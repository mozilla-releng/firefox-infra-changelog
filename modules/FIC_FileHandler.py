# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


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

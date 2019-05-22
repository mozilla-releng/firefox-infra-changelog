# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_DataVault import FICDataVault
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Utilities import return_time
from modules.config import COMMIT_DESCRIPTION_LENGTH, CHANGELOG_REPO_PATH
import json


class FICMarkdownGenerator(FICFileHandler, FICDataVault):
    def __init__(self):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.md_ready_data = []

    @staticmethod
    def _get_current_time():
        return return_time(time_format="%Y-%m-%dT%H:%M:%S")

    def _load_local_json_data(self):
        return json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json"))

    def _build_initial_md_structure(self):
        self.md_ready_data.append(self._create_repo_markdown_header())
        self.md_ready_data.append(self._create_first_table_row())

    def _create_repo_markdown_header(self):
        return "## " + self.repo_name + " MD table" + "\n" + "Generated on: {}".format(self._get_current_time()) + "\n\n"

    @staticmethod
    def _create_first_table_row():
        return "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
               "|:-----:|:-----:|:----------------------------------:|:------:|:----:| \n"

    def md_table_row_builder(self):
        return "|" + str(self.commit_number) + "|" + self.commit_author + "|" + self.commit_message + \
               "|" + "[URL](" + self.commit_url + ")" + "|" + str(self.commit_date) + "\n"

    def generate_link_for_bugs(self):
        import re

        commit_msg = re.sub("\(", "( ", self.commit_message)
        commit_msg = re.sub("\)", " )", commit_msg)

        list_of_words = commit_msg.split()

        for element in range(len(list_of_words)):
            if "bug" in (list_of_words[element].lower()) and list_of_words[element + 1].isdigit():
                bug_number = list_of_words[element + 1]
                generated_link = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + bug_number
                list_of_words[element] = '[' + 'Bug' + ' ' + bug_number + '](' + generated_link + ')'
                list_of_words[element + 1] = ''

        self.commit_message = ' '.join(list_of_words)
        return self.commit_message

    def filter_strings(self):
        """
        Filters the provided string and removes specific words/characters from it
        that are stored in unwanted_chars variable.
        This filter removes chars that can't be written to the markdown file
        (since the encoding of those is not supported).
        :param string: string to be filtered
        :return:
        """
        import re

        unwanted_chars = ["\u0131", "\u30c4", "\u00c1", "\u00ee", "\u0103",
                          "\u00e4", "\u00e8", "\u2013", "\U0001f60b", "\u00af",
                          "\U0001f92a"]

        # Prepare author name for
        for word in self.commit_author:
            if word in unwanted_chars:
                self.commit_author = re.sub(word, "", self.commit_author)

        for word in self.commit_message:
            if word in unwanted_chars:
                self.commit_message = re.sub(word, "", self.commit_message)

        return self.commit_author, self.commit_message

    def trim_commit_description(self, commit_link, length=COMMIT_DESCRIPTION_LENGTH):
        if len(self.commit_message) > length:
            self.commit_message = self.commit_message[0:length] + ".. [continue reading](" + commit_link + ")"
        return self.commit_message

    def _populate_md_table(self):
        local_json_data = self._load_local_json_data()
        if len(local_json_data) > 0:
            del local_json_data["0"]
            self.commit_number = 1
            for key in local_json_data:
                self.commit_date = local_json_data.get(key).get("date")
                if self.commit_date > return_time("%Y-%m-%dT%H:%M:%S", "sub", 7):
                    self.commit_author = local_json_data.get(key).get("author")
                    self.commit_url = local_json_data.get(key).get("url")
                    self.commit_message = local_json_data.get(key).get("message")
                    self.commit_author, self.commit_message = self.filter_strings()
                    self.trim_commit_description(self.commit_url, COMMIT_DESCRIPTION_LENGTH)
                    self.generate_link_for_bugs()
                    self.md_ready_data.append(self.md_table_row_builder())
                    self.commit_number += 1
        else:
            print("No commits in the past 7 days")  # to be replace with a method

    def start_md_for_git(self, repo_name=None):
        self.repo_name = repo_name
        self._build_initial_md_structure()
        self._populate_md_table()
        for element in a.md_ready_data:
            print(element)
            a.save(CHANGELOG_REPO_PATH, a.repo_name + ".md", element)


# TESTING BELOW

a = FICMarkdownGenerator()
a.start_md_for_git("taskcluster")

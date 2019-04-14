# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_DataVault import FICDataVault
from modules.FIC_FileHandler import FICFileHandler
from modules.config import COMMIT_DESCRIPTION_LENGTH


class FICMarkdownGenerator(FICFileHandler, FICDataVault):
    def __init__(self):
        FICDataVault.__init__(self)
        FICFileHandler.__init__(self)
        self._current_time = self._get_current_time()
        self.markdown_file_header = self._create_repo_markdown_header()
        self.first_table_row = self.create_first_table_row()
        self.md_table_row = self.md_table_row_builder
        self.changelog_table_header = None
        self.trimmed_commit_message = self.trim_commit_message()
        self.linked_commit_msg = self.generate_link_for_bugs(self.commit_message)

    @staticmethod
    def _get_current_time():
        import datetime
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    def _create_repo_markdown_header(self):
        return self.repo_name + " MD table" + "\n" + "Generated on: {}".format(self._current_time)

    @staticmethod
    def create_first_table_row():
        first_row_string = "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
                           "|:---:|:----:|:----------------------------------:|:------:|:----:| \n"
        return first_row_string

    @property
    def md_table_row_builder(self):
        return "|" + str(self.commit_number) + "|" + self.commit_author + "|" + self.commit_message + \
                      "|" + "[URL](" + self.commit_url + ")" + "|" + str(self.commit_date) + "\n"

    def trim_commit_message(self):
        return self.commit_message[:COMMIT_DESCRIPTION_LENGTH]

    def write_markdown(self, directory, file_name):
        self.save(directory, file_name, "CONTENT HERE")

    @staticmethod
    def generate_link_for_bugs(commit_msg):
        import re
        list_of_words = commit_msg.split()
        for element in range(len(list_of_words)):
            if "bug" in (list_of_words[element].lower()) and element < len(list_of_words) - 1:
                bug_number = re.sub("[(:,.;)]", "", list_of_words[element + 1])
                bug_number = int(''.join(list(filter(str.isdigit, bug_number))))
                generated_link = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + \
                                 str(bug_number)
                list_of_words[element] = '[' + 'Bug' + ' ' + str(
                    bug_number) + '](' + generated_link + ')'
                list_of_words[element + 1] = ''
        commit_text = ' '.join(list_of_words)
        return commit_text

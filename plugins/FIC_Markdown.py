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
        # self.markdown_file_header = self._create_repo_markdown_header()
        self.first_table_row = self.create_first_table_row()
        self.md_table_row = self.md_table_row_builder
        self.changelog_table_header = None
        self.trimmed_commit_message = self.trim_commit_message()
        self.linked_commit_url = None
        self.linked_commit_auhor = None

    @staticmethod
    def _get_current_time():
        import datetime
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # def _create_repo_markdown_header(self):
    #     return self.repo_name + " MD table" + "\n" + "Generated on: {}".format(self._current_time)

    @staticmethod
    def create_first_table_row():
        first_row_string = "| Commit Number | Commiter | Commit Message | Commit Url | Date | \n" + \
                           "|:---:|:----:|:----------------------------------:|:------:|:----:| \n"
        return first_row_string

    def md_table_row_builder(self):
        return "|" + self.commit_number + "|" + self.commit_author + "|" + self.commit_message + \
                      "|" + "[URL](" + self.commit_url + ")" + "|" + self.commit_date + "\n"

    def trim_commit_message(self):
        return trim_commit_description(self.commit_message, COMMIT_DESCRIPTION_LENGTH)

    def write_markdown(self, directory, file_name):
        self.save(directory, file_name, "CONTENT HERE")



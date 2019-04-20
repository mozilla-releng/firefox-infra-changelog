from modules.FIC_DataVault import FICDataVault
from modules.config import COMMIT_DESCRIPTION_LENGTH
import re
import os


class FicFiltering(FICDataVault):

    def __init__(self):
        FICDataVault.__init__(self)
        self.formated_string = None

    def filter_strings(self, string):
        """
        Filters the provided string and removes specific words/characters from it
        that are stored in unwanted_chars variable.
        This filter removes chars that can't be written to the markdown file
        (since the encoding of those is not supported).
        :param string: string to be filtered
        :return:
        """
        unwanted_chars = ["\u0131", "\u30c4", "\u00c1", "\u00ee", "\u0103",
                          "\u00e4", "\u00e8", "\u2013", "\U0001f60b", "\u00af",
                          "\U0001f92a"]

        for word in string:
            if word in unwanted_chars:
                self.formated_string = re.sub(word, " ", string)
                return self.formated_string

    def trim_commit_description(self, commit_link, length=COMMIT_DESCRIPTION_LENGTH):
        if len(self.commit_message) > length:
            self.commit_message = self.commit_message[0:length] + ".. [continue reading](" + commit_link + ")"
        return self.commit_message

    def replace_bug_with_url(self):
        commit_text = self.commit_message.split()
        for element in range(len(commit_text)):
            if "bug" in (commit_text[element].lower()) and element < len(commit_text) - 1:
                bug_number = re.sub("[(:,.;)]", "", commit_text[element + 1])
                try:
                    bug_number = int(''.join(list(filter(str.isdigit, bug_number))))
                    generated_link = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + \
                                     str(bug_number)
                    commit_text[element] = '[' + 'Bug' + ' ' + str(bug_number) + '](' + generated_link + ')'
                    commit_text[element + 1] = ''
                except ValueError:
                    # if LOGGER.root.level == 30:
                    #     LOGGER.warning("Invalid bug number: > {} < in message: {}"
                    #                    .format(commit_text[element + 1], message))
                    pass
        self.commit_message = ' '.join(commit_text)
        return self.commit_message

    # def rename_element_with_date(self, file_name, date_string):
    #     """
    #     Implemented in: issue-390
    #     Function that is used to rename a file and add a date to the title.
    #     Use case:
    #     rename_element_with_dt((os.pardir + r"\test_file.md"), "20190323")
    #     or
    #     rename_element_with_dt("git_files/addonscript.md", "20190323")
    #     :param logger: logger object to log the rename.
    #     :param file_name: name or path+name of the file to be renamed
    #     :param date_string:
    #     :return:
    #     """
    #     generated_name = str(file_name[0:-3]) + "." + date_string + ".md"
    #     try:
    #         os.rename(file_name, generated_name)
    #     except os.error:
    #     #     logger.error("Failed to rename the provided file {}".format(file_name))
    #     # logger.info("Renamed element {} into {}."
    #     #             .format(file_name, generated_name))
    #         pass
    #     return self.generated_name
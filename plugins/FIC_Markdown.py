# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_DataVault import FICDataVault
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Utilities import return_time
from modules.config import COMMIT_DESCRIPTION_LENGTH, CHANGELOG_REPO_PATH, DEFAULT_DAYS, CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, REPOSITORIES_FILE
import json


class FICMarkdownGenerator(FICFileHandler, FICDataVault):
    def __init__(self):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.md_ready_data = []
        self.changelog_md_data = []

    @staticmethod
    def _get_current_time():
        return return_time(output_time_format="%Y-%m-%dT%H:%M:%S")

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

    def _generate_repo_url(self, repository_type):
        repositories_data = json.load(self.load(None, REPOSITORIES_FILE))
        return repositories_data.get(repository_type).get(self.repo_name).get("url")

    def no_data_for_md(self, argument, main_markdown=False, repo_markdown=False):
        if main_markdown:
            return f"| No commits in the past {DEFAULT_DAYS} days.. see the longer history [here]({argument}) |\n"
        elif repo_markdown:
            return f"| No recent changes on this repository.. see the entire changelog by accessing this [link]({self._generate_repo_url(argument)}) |"

    def generate_link_for_bugs(self):
        import re

        commit_msg = re.sub("\(", "( ", self.commit_message)
        commit_msg = re.sub("\)", " )", commit_msg)

        list_of_words = commit_msg.split()
        for element in range(len(list_of_words)):
            if "bug" in (list_of_words[element].lower()) and element < len(list_of_words) - 1:
                bug_number = re.sub("[(:,.;)]", "", list_of_words[element + 1])
                try:
                    bug_number = int(''.join(list(filter(str.isdigit, bug_number))))
                    generated_link = "https://bugzilla.mozilla.org/show_bug.cgi?id=" + \
                                     str(bug_number)
                    list_of_words[element] = '[' + 'Bug' + ' ' + str(bug_number) + '](' + generated_link + ')'
                    list_of_words[element + 1] = ''
                except ValueError:
                    pass

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
                          "\U0001f92a", "\n"]

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

    def _populate_md_for_git(self):
        local_json_data = self._load_local_json_data()
        if len(local_json_data) > 1:
            del local_json_data["0"]
            self.commit_number = 1
            for key in local_json_data:
                self.commit_date = return_time(input_time=local_json_data.get(key).get("date"), input_time_format="%Y-%m-%dT%H:%M:%SZ", output_time_format="%Y-%m-%d %H:%M:%S")
                self.commit_author = local_json_data.get(key).get("author")
                self.commit_url = local_json_data.get(key).get("url")
                self.commit_message = local_json_data.get(key).get("message")
                self.commit_author, self.commit_message = self.filter_strings()
                self.trim_commit_description(self.commit_url, COMMIT_DESCRIPTION_LENGTH)
                self.generate_link_for_bugs()
                self.md_ready_data.append(self.md_table_row_builder())
                self.commit_number += 1
        else:
            self.md_ready_data.append(self.no_data_for_md("Github", repo_markdown=True))

    def start_md_for_git(self, repo_name=None):
        self.repo_name = repo_name
        open(self.construct_path(CHANGELOG_REPO_PATH, repo_name + ".md"), 'w').close()
        self._build_initial_md_structure()
        self._populate_md_for_git()
        for element in self.md_ready_data:
            self.save(CHANGELOG_REPO_PATH, repo_name + ".md", element)
        self.md_ready_data = []

    def _populate_md_for_hg(self):
        local_json_data = self._load_local_json_data()
        if len(local_json_data) > 1:
            del local_json_data["0"]
            self.commit_number = 1
            for changeset in local_json_data:
                for commit in local_json_data.get(changeset).get("changeset_commits"):
                    self.commit_date = return_time(input_time=local_json_data.get(changeset).get("date_of_push"), input_time_format="%Y-%m-%dT%H:%M:%S.%f", output_time_format="%Y-%m-%d %H:%M:%S")
                    self.commit_author = local_json_data.get(changeset).get("changeset_commits").get(commit).get("commit_author").split("<")[0]
                    self.commit_url = local_json_data.get(changeset).get("changeset_commits").get(commit).get("url")
                    self.commit_message = local_json_data.get(changeset).get("changeset_commits").get(commit).get("commit_message")
                    self.commit_author, self.commit_message = self.filter_strings()
                    self.trim_commit_description(self.commit_url, COMMIT_DESCRIPTION_LENGTH)
                    self.generate_link_for_bugs()
                    self.md_ready_data.append(self.md_table_row_builder())
                    self.commit_number += 1
        else:
            self.md_ready_data.append(self.no_data_for_md("Mercurial", repo_markdown=True))

    def start_md_for_hg(self, repo_name=None):
        self.repo_name = repo_name
        open(self.construct_path(CHANGELOG_REPO_PATH, repo_name + ".md"), 'w').close()
        self._build_initial_md_structure()
        self._populate_md_for_hg()
        for element in self.md_ready_data:
            self.save(CHANGELOG_REPO_PATH, repo_name + ".md", element)
        self.md_ready_data = []

    def _changelog_md_header(self):
        return "## " + "Commits in production - for {} days".format(DEFAULT_DAYS) + "\n" + "### " + "Generated on: {}".format(self._get_current_time()) + "\n"

    @staticmethod
    def _changelog_md_links(repo, json_link, md_link):
        return "\n | {} |".format(repo) + "[Markdown](" + md_link + ")" + "|" + "[Json](" + json_link + ")" + "| \n" + \
               "|:----------:|:-----------------------:|:--------:| \n\n"

    @staticmethod
    def _changelog_md_first_row():
        return "| Link | Last commit | Author | Reviewer | Deploy time | \n" + \
               "|:----------:|:-----------:|:------:|:--------:|:-----------:| \n"

    @staticmethod
    def _get_display_order(changelog_data, repo_config):
        repo_order = []
        for element in changelog_data["Github"]:
            order = repo_config["Github"][element]["order"]
            repo_order.append((element, order, "git"))
        for element in changelog_data["Mercurial"]:
            order = repo_config["Mercurial"][element]["order"]
            repo_order.append((element, order, "hg"))
        repo_order.sort(key=lambda tup: tup[1])
        return repo_order

    def extract_reviewer(self):
        try:
            return self.commit_message.split("r=")[1].split()[0]
        except IndexError:
            pass

        try:
            return self.commit_message.split("a=")[1].split()[0]
        except IndexError:
            pass

        return "N/A"

    @staticmethod
    def _get_js_md_links(repo):
        base_link = "https://github.com/mozilla-releng/firefox-infra-changelog/tree/oop/data/"
        return base_link + repo + ".json", base_link + repo + ".md"

    def _changelog_md_row_builder(self):
        return "|" + "[Link](" + self.commit_url + ")" + "|" + str(self.generate_link_for_bugs()) + "|" + self.commit_author + \
               "|" + str(self.commit_reviewer) + "|" + str(self.commit_date) + "\n"

    def _populate_changelog_md(self, element, changelog_data):
        json_link, md_link = self._get_js_md_links(element[0])
        if element[2] is "git":
            self.changelog_md_data.append(self._changelog_md_links(element[0], json_link, md_link))
            self.changelog_md_data.append(self._changelog_md_first_row())
            if len(changelog_data["Github"][element[0]]) > 0:
                for value in changelog_data["Github"][element[0]].values():
                    self.commit_url = value["url"]
                    self.commit_message = value["message"]
                    self.commit_author = value["author"]
                    self.commit_reviewer = "N/A"
                    self.commit_date = return_time(input_time=value["date"], input_time_format="%Y-%m-%dT%H:%M:%SZ", output_time_format="%Y-%m-%d %H:%M:%S")
                    self.commit_author, self.commit_message = self.filter_strings()
                    self.changelog_md_data.append(self._changelog_md_row_builder())
            else:
                self.changelog_md_data.append(self.no_data_for_md(md_link, main_markdown=True))
        if element[2] is "hg":
            self.changelog_md_data.append(self._changelog_md_links(element[0], json_link, md_link))
            self.changelog_md_data.append(self._changelog_md_first_row())
            if len(changelog_data["Mercurial"][element[0]]) > 0:
                for value in changelog_data["Mercurial"][element[0]].values():
                    self.commit_date = return_time(input_time=value["date_of_push"], input_time_format="%Y-%m-%dT%H:%M:%S.%f", output_time_format="%Y-%m-%d %H:%M:%S")
                    for commit in value["changeset_commits"].values():
                        self.commit_url = commit["url"]
                        self.commit_message = commit["commit_message"]
                        self.commit_author = commit["commit_author"].split("<")[0]
                        self.commit_reviewer = self.extract_reviewer()
                        self.commit_author, self.commit_message = self.filter_strings()
                        self.changelog_md_data.append(self._changelog_md_row_builder())
            else:
                self.changelog_md_data.append(self.no_data_for_md(md_link, main_markdown=True))

    def create_changelog_md(self):
        open(self.construct_path(None, CHANGELOG_MD_PATH), 'w').close()
        changelog_data = json.load(self.load(None, CHANGELOG_JSON_PATH))
        repo_config = json.load(self.load(None, REPOSITORIES_FILE))
        repo_order = self._get_display_order(changelog_data, repo_config)
        self.changelog_md_data.append(self._changelog_md_header())
        for element in repo_order:
            self._populate_changelog_md(element, changelog_data)
        for element in self.changelog_md_data:
            self.save(None, CHANGELOG_MD_PATH, element)

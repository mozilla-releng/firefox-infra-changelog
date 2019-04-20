# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_DataVault import FICDataVault
import json
import requests


class FICMercurial(FICFileHandler, FICDataVault):

    def __init__(self, file_name, repo_name):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.file_name = file_name
        self.repo_name = repo_name
        self.directory = "../"  # Hardcoded for now. We will need to pass this dynamically.
        self.repo_data = self._load_json("../data/", self.file_name)  # Hardcoded directory for now. We will need to pass this dynamically.

    def start(self):
        self._prepare_url()
        self._download_data()
        self._store_data()

    # =======PREPARE URL========
    def _prepare_url(self):
        self._load_json("../data/", self.file_name)
        self._get_last_local_push_id()
        self._load_repository_data(self.directory)
        self._get_repo_link(self.repo_name)
        self._request_hg_data()
        self._load_response_in_json()
        self._get_end_id()
        self._generate_push_link()
        self._download_data()

    # =========DOWNLOAD DATA========
    def _download_data(self):
        self._request_changesets_data()
        self._load_changesets_data_in_json()
        self._store_data()

    # =========STORE DATA==========
    def _store_data(self):
        self._get_pushes_number()
        self._get_changeset_date()
        self._get_changeset_lander()
        self._get_commits()
        self._get_author()
        self._get_description()
        self._get_changed_files()
        self._construct_commit_url()
        self._get_changeset_number()
        self._get_changesets_commits()
        self._construct_commits_dict()

    def _construct_commit_url(self):
        self._get_node()
        self._generate_commit_url()

    # Load local .json file
    def _load_json(self, directory, file_name):
        self.load_local_json = json.load(self.load(directory, file_name))
        return self.load_local_json

    # Get last push id from local file
    def _get_last_local_push_id(self):
        self.last_local_push_id = self.load_local_json.get("0").get("last_push_id")
        return self.last_local_push_id

    # Loads repositories.json
    def _load_repository_data(self, directory):
        self.load_repositories = json.load(self.load(directory, "repositories.json"))
        return self.load_repositories

    # Get repo link for specific repo we need
    def _get_repo_link(self, repo_name):
        self.repository_url = self.load_repositories.get("Mercurial").get(repo_name).get("url")
        return self.repository_url

    # Request hg data to find last remote push id
    def _request_hg_data(self):
        url_flags = "json-pushes?version=2&full=1&startID=3&endID=5"
        self.hg_response = requests.get(self.repository_url + url_flags).text
        return self.hg_response

    # Format response into json
    def _load_response_in_json(self):
        self.response_json = json.loads(self.hg_response)
        return self.response_json

    # Actually get lastpushid from remote
    def _get_end_id(self):
        self.end_id = self.response_json.get("lastpushid")
        return self.end_id

    # Using previous data generates a download link
    def _generate_push_link(self):
        url_options = "json-pushes?version=2&full=1&startID={}&endID={}".format(self.last_local_push_id, self.end_id)
        self.push_link = self.repository_url + url_options
        return self.push_link

    # Requests data from hg using a link generated on difference between remote and local
    def _request_changesets_data(self):
        self.changesets_response = requests.get(self.push_link).text
        return self.changesets_response

    # Format response into json
    def _load_changesets_data_in_json(self):
        self.changesets_json = json.loads(self.changesets_response)
        return self.changesets_json

    # Picks up changesets for picking up changeset author, date
    def _get_pushes_number(self):
        for number in self.changesets_json.get("pushes"):
            self.changeset = self.changesets_json.get("pushes").get(number)
            return self.changeset

    # Picks up date and formats it
    def _get_changeset_date(self):
        import time
        unformated_date = self.changeset.get("date")
        self.changeset_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unformated_date))
        return self.changeset_date

    # Gets changeset_author
    def _get_changeset_lander(self):
        self.changeset_lander = self.changeset.get("user")
        return self.changeset_lander

    # Gets all the commits from a changeset
    def _get_commits(self):
        for commit in range(0, len(self.changeset.get("changesets"))):
            self.commits = self.changeset.get("changesets")[commit]
            return self.commits

    # Gets author from commits
    def _get_author(self):
        self.commit_author = self.commits.get("author")
        return self.commit_author

    # Gets description from commits
    def _get_description(self):
        self.commit_message = self.commits.get("desc")
        return self.commit_message

    # Gets files changed from commit
    def _get_changed_files(self):
        self.commit_files_changed = [file for file in self.commits.get("files")]
        return self.commit_files_changed

    # Get hash, laster used to format commit url
    def _get_node(self):
        self.commit_sha = self.commits.get("node")
        return self.commit_sha

    # Generated commit url by triming hash
    def _generate_commit_url(self):
        self.commit_url = self.repository_url + "pushloghtml?changeset=" + self.commit_sha[:12]
        return self.commit_url

    # Changeset number
    def _get_changeset_number(self):
        for key in self.changesets_json.get("pushes"):
            self.changeset_number = key
            return self.changeset_number

    # Get changeset commits as list
    def _get_changesets_commits(self):
        for key in self.changesets_json.get("pushes").get(self.changeset_number):
            self.changeset_commits = self.changesets_json.get("pushes").get(self.changeset_number).get(key)
            return self.changeset_commits

    # Construct commit dictionary per changeset
    def _construct_commits_dict(self):
        self.hg_commits_list = {}
        for commit in range(len(self.changeset_commits)):
            self.hg_commits_list.update({commit + 1: {"url": self.commit_url,
                                 "commiter_author": self.commit_author,
                                 "commit_message": self.commit_message,
                                 "files_changed": self.commit_files_changed}})
        return self.hg_commits_list


a = FICMercurial("mozilla-central.json", "mozilla-central")
a.start()
print("json")
# ^^ Here for testing propose
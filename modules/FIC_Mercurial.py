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
        self.start_id = self._get_last_local_push_id()
        self.repository_data = self._load_repository_data(self.directory)
        self.repository_url = self._get_repo_link(self.repo_name)
        self.hg_response = self._request_hg_data()
        self.response_json = self._load_response_in_json()
        self.end_id = self._get_end_id()
        self.push_link = self._generate_push_link()
        self.changesets_response = self._request_changesets_data()
        self.changesets_json = self._load_changesets_data_in_json()

        # Last push id
        self.last_push_id = self._get_last_push_id()

        # Number of changeset
        self.changeset = self._get_pushes()

        # Name of the person who landed changeset
        self.changeset_lander = self._get_changeset_lander()

        # Date when changeset was pushed
        self.changeset_date = self._get_changeset_date()

        # Index of commits
        self.commits = self._get_commits()

        # Commit author
        self.commit_author = self._get_author()

        # Commit description
        self.commit_message = self._get_description()

        # Changed files
        self.commit_files_changed = self._get_changed_files()
        self.commit_sha = self._get_node()

        # Commit url
        self.commit_url = self._generate_commit_url()

    def _load_json(self, directory, file_name):
        return json.load(self.load(directory, file_name))

    def _get_last_local_push_id(self):
        return self.repo_data.get("0").get("last_push_id")

    def _load_repository_data(self, directory):
        return json.load(self.load(directory, "repositories.json"))

    def _get_repo_link(self, repo_name):
        return self.repository_data.get("Mercurial").get(repo_name).get("url")

    def _request_hg_data(self):
        url_flags = "json-pushes?version=2&full=1&startID=3&endID=5"
        return requests.get(self.repository_url + url_flags).text

    def _load_response_in_json(self):
        return json.loads(self.hg_response)

    def _get_end_id(self):
        return self.response_json.get("lastpushid")

    def _generate_push_link(self):
        url_options = "json-pushes?version=2&full=1&startID={}&endID={}".format(self.start_id, self.end_id)
        return self.repository_url + url_options

    def _request_changesets_data(self):
        return requests.get(self.push_link).text

    def _load_changesets_data_in_json(self):
        return json.loads(self.changesets_response)

    def _get_last_push_id(self):
        return self.changesets_json.get("lastpushid")

    def _get_pushes(self):
        for number in self.changesets_json.get("pushes"):
            return self.changesets_json.get("pushes").get(number)

    def _get_changeset_date(self):
        import time
        unformated_date = self.changeset.get("date")
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(unformated_date))

    def _get_changeset_lander(self):
        return self.changeset.get("user")

    def _get_commits(self):
        for commit in range(0, len(self.changeset.get("changesets"))):
            return self.changeset.get("changesets")[commit]

    def _get_author(self):
        return self.commits.get("author")

    def _get_description(self):
        return self.commits.get("desc")

    def _get_changed_files(self):
        file_list = [file for file in self.commits.get("files")]
        return file_list

    def _get_node(self):
        return self.commits.get("node")

    def _generate_commit_url(self):
        return self.repository_url + "pushloghtml?changeset=" + self.commit_sha[:12]


a = FICMercurial("mozilla-central.json", "mozilla-central")


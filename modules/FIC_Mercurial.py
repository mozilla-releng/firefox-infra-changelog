# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_DataVault import FICDataVault
from modules.FIC_Utilities import return_time
import json
import requests
from modules.config import CHANGELOG_REPO_PATH, HG_CHANGESETS_TO_SHOW, REPOSITORIES_FILE


class FICMercurial(FICFileHandler, FICDataVault):
    def __init__(self):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)

    def start_hg(self, repo_name):
        self.repo_name = repo_name
        self.file_name = repo_name + ".json"
        self.folders_to_check = self._repo_files_hg()
        self.repo_data = json.load(self.load(None, REPOSITORIES_FILE))
        self.local_repo_data = json.load(self.load(CHANGELOG_REPO_PATH, self.file_name))
        self._prepare_url()
        self._download_data()
        self._construct_json_dict()

    # =======PREPARE URL========
    def _prepare_url(self):
        self._get_repo_link(self.repo_name)
        self._request_hg_data()
        self._load_response_in_json()
        self._get_end_id()
        self._generate_push_link()

    # =========DOWNLOAD DATA========
    def _download_data(self):
        self._request_changesets_data()
        self._load_changesets_data_in_json()

    # Get last push id from local file
    def _get_last_local_push_id(self):
        self.last_local_push_id = self.local_repo_data.get("0").get("last_push_id")
        return self.last_local_push_id

    # Get repo link for specific repo we need
    def _get_repo_link(self, repo_name):
        self.repository_url = self.repo_data.get("Mercurial").get(repo_name).get("url")
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
        if self.local_repo_data.get("0"):
            self._get_last_local_push_id()
            url_options = "json-pushes?version=2&full=1&startID={}&endID={}".format(self.last_local_push_id, self.end_id)
        else:
            url_options = "json-pushes?version=2&full=1&startID={}&endID={}".format(self.end_id - HG_CHANGESETS_TO_SHOW, self.end_id)
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

    # Picks up date and formats it
    def _generate_changeset_date(self, date):
        self.changeset_date = return_time("%Y-%m-%dT%H:%M:%S.%f")
        return self.changeset_date

    # Generated commit url by triming hash
    def _generate_commit_url(self, node):
        self.commit_url = self.repository_url + "pushloghtml?changeset=" + node[:12]
        return self.commit_url

    def _repo_files_hg(self):
        self.folders_to_check = json.load(self.load(None, REPOSITORIES_FILE)).get("Mercurial").get(self.repo_name).get("configuration").get("folders-to-check")
        return self.folders_to_check

    def _compare_files(self):
        for folder_to_check in range(len(self.folders_to_check)):
            for changed_folder in range(len(self.commit_files_changed)):
                if str(self.folders_to_check[folder_to_check]) in str(self.commit_files_changed[changed_folder]):
                    return True

    def _prep_final_dict(self):
        self.final_dict = {}
        self.final_dict.update({"0": {"last_push_id": self.end_id}})

    def _get_local_data(self):
        if len(self.local_repo_data):
            self.local_repo_data.pop("0")
            for key, value in self.local_repo_data.items():
                self.list_of_dicts.append(value)

    def _add_changeset_data(self, push):
        unformated_date = self.changesets_json.get("pushes").get(push).get("date")
        pusher = self.changesets_json.get("pushes").get(push).get("user")
        date = self._generate_changeset_date(unformated_date)
        self.changeset_dict.update({"pusher": pusher, "date_of_push": date, "changeset_commits": {}})

    def _add_commit_data(self, push, commit):
        self.commit_files_changed = self.changesets_json.get("pushes").get(push).get("changesets")[commit]["files"]
        if self._compare_files():
            node = self.changesets_json.get("pushes").get(push).get("changesets")[commit]["node"]
            commit_author = self.changesets_json.get("pushes").get(push).get("changesets")[commit]["author"]
            commit_message = self.changesets_json.get("pushes").get(push).get("changesets")[commit]["desc"]
            self.changeset_dict["changeset_commits"].update(
                {commit + 1: {"url": self._generate_commit_url(node),
                              "commit_author": commit_author,
                              "commit_message": commit_message,
                              "files_changed": self.commit_files_changed}})

    def _populate_final_dict(self):
        for changeset in reversed(self.list_of_dicts):
            if len(changeset["changeset_commits"]) == 0:
                del changeset
            else:
                self.push_number += 1
                self.final_dict.update({self.push_number: changeset})

    # Construct json dictionary
    def _construct_json_dict(self):
        self.list_of_dicts = []
        self._prep_final_dict()
        self.push_number = 0
        self._get_local_data()
        for push in self.changesets_json.get("pushes"):
            self.changeset_dict = {}
            self._add_changeset_data(push)
            for commit in range(len(self.changesets_json.get("pushes").get(push).get("changesets"))):
                self._add_commit_data(push, commit)
            self.list_of_dicts.append(self.changeset_dict)

        self._populate_final_dict()
        self.save(CHANGELOG_REPO_PATH, self.repo_name + ".json", self.final_dict)

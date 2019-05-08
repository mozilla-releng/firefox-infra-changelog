# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_DataVault import FICDataVault
from modules.config import GIT_TOKEN
from modules.config import CHANGELOG_REPO_PATH
from git import Repo
import os
import json


class FICGithub(FICFileHandler, FICDataVault):
    def __init__(self):
        FICFileHandler.__init__(self)
        FICDataVault.__init__(self)
        self.token_counter = 0
        self._get_os_var()
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.repo_data = None
        self.repo = Repo("..")

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self):
        return self._init_github(self._gh, self.team_name, self.repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def _get_os_var(self):
        for var in os.environ:
            # append the OS.VAR to the list in case of no duplicate
            if "GIT_TOKEN" in var and var not in GIT_TOKEN:
                GIT_TOKEN.append(var)
        self.LOGGER.info("The list of available tokens: %s", GIT_TOKEN)

    def _get_reset_time(self):
        from datetime import datetime
        reset_time = datetime.fromtimestamp(self._gh.rate_limit()['rate']['reset'])
        self.LOGGER.info("Rate limit reset in: %s", reset_time - datetime.now())
        return reset_time

    def limit_checker(self):
        limit_requests = self._gh.ratelimit_remaining

        if limit_requests < 5 and len(GIT_TOKEN) > 1:
            # switch token
            if self._switch_token():
                return True
            else:
                # check if the rate limit was reset for the second use of a token
                if limit_requests < 5:
                    print(self._get_reset_time())
                    return False
                else:
                    return True
        # check the reset time in case of a single token
        elif limit_requests < 5:
            print(self._get_reset_time())
            return False
        # return True in case of limit request not reached
        else:
            return True

    def _switch_token(self):
        # get next token
        switch = self._get_token()
        # re-logging with the new token
        self._token = os.environ.get(GIT_TOKEN[self.token_counter])
        self._gh = self._auth()
        self.LOGGER.info("The token was changed.")
        return switch

    def _get_token(self):
        # in case of the next token but not the last
        if self.token_counter < len(GIT_TOKEN) - 1:
            self.token_counter += 1
            self.LOGGER.info("Changing token with: %s", GIT_TOKEN[self.token_counter])
            return True
        # in case of the last token
        elif self.token_counter == len(GIT_TOKEN) - 1:
            self.token_counter = 0
            self.LOGGER.info("Changing token with: %s", GIT_TOKEN[self.token_counter])
            return False

    def pull(self):
        self.LOGGER.info("pulling changes from {} -> Branch {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
        return self.repo.remotes.origin.pull(refspec=self.repo.active_branch)

    def add(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        self.repo.git.add([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH], update=True)
        return self.check_for_changes()

    def check_for_changes(self):
        if not self.repo.index.diff("HEAD"):
            self.LOGGER.info("Nothing staged for commit. has the data or files changed?")
            return False
        return True

    def commit(self):
        from datetime import datetime
        self.LOGGER.info("Committing changes with message: Changelog: %s", str(datetime.utcnow()))
        return self.repo.index.commit("Changelog: " + str(datetime.utcnow()))

    def push(self):
        self.LOGGER.info("Summary of pull: {}".format(FICGithub.pull(self)[0]))
        if FICGithub.add(self):
            self.LOGGER.info("Summary of commit {}".format(FICGithub.commit(self)))
            self.LOGGER.info("pushing changes to {}  on branch  {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
            self.LOGGER.info("Summary of push: {}".format(self.repo.remotes.origin.push(refspec=self.repo.active_branch)[0].summary))

    def revert_modified_files(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        return self.repo.git.checkout([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH])

    def get_repo_url(self):
        return self.repo_data.svn_url

    def _repo_team(self):
        self.team_name = json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("team")

    def _repo_files(self):
        self.folders_to_check = json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("configuration").get("folders-to-check")

    def _extract_repo_type(self):
        self.repo_type = json.load(self.load(None, "repositories.json")).get("Github").get(self.repo_name).get("configuration").get("type")

    def _local_version(self):
        self.local_version = json.load(self.load(CHANGELOG_REPO_PATH, self.repo_name.lower() + ".json")).get("0").get("last_release").get("version")
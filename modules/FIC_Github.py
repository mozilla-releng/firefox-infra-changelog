# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_Logger import FICLogger
from modules.config import GIT_TOKEN
from git import Repo
import os


class FICGithub(FICLogger):
    def __init__(self):
        FICLogger.__init__(self)
        self.token_counter = 0
        self._token = None
        self._gh = None
        self.repo_data = None
        self.repo = Repo("..")
        self._available_tokens = []
        self.token_handler()

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self, team_name, repo_name):
        return self._init_github(self._gh, team_name, repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def _get_os_var(self):
        for var in os.environ:
            # append the OS.VAR to the list in case of no duplicate
            if GIT_TOKEN in var:
                self._available_tokens.append(var)
        self.LOGGER.debug("The list of available tokens: %s", self._available_tokens)

    def _get_reset_time(self):
        from datetime import datetime
        reset_time = datetime.fromtimestamp(self._gh.rate_limit()['rate']['reset'])
        self.LOGGER.info("Rate limit reset in: %s", reset_time - datetime.now())
        return reset_time

    def limit_checker(self):
        limit_requests = self._gh.ratelimit_remaining
        if limit_requests < 5:
                return False

    def _switch_token(self):
        if self.token_counter < len(self._available_tokens):
            if self.token_counter == len(self._available_tokens) - 1:
                self.token_counter = -1
            # get next token and re-log with it
            self.token_counter += 1
            self._token = os.environ.get(self._available_tokens[self.token_counter])
            self._gh = self._auth()
            self.LOGGER.info("Changing token with: %s", self._available_tokens[self.token_counter])
            if self._gh.ratelimit_remaining > 5:
                return True
            else:
                return False

    def pull(self):
        self.LOGGER.debug("pulling changes from {} -> Branch {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
        return self.repo.remotes.origin.pull(refspec=self.repo.active_branch)

    def add(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        self.repo.git.add([CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH], update=True)
        return self.check_for_changes()

    def check_for_changes(self):
        if not self.repo.index.diff("HEAD"):
            self.LOGGER.debug("Nothing staged for commit. has the data or files changed?")
            return False
        return True

    def commit(self):
        from datetime import datetime
        self.LOGGER.info("Committing changes with message: Changelog: %s", str(datetime.utcnow()))
        return self.repo.index.commit("Changelog: " + str(datetime.utcnow()))

    def push(self):
        self.LOGGER.debug("Summary of pull: {}".format(FICGithub.pull(self)[0]))
        if FICGithub.add(self):
            self.LOGGER.debug("Summary of commit {}".format(FICGithub.commit(self)))
            self.LOGGER.debug("pushing changes to {}  on branch  {}".format(self.repo.remotes.origin.url, self.repo.active_branch))
            self.LOGGER.debug("Summary of push: {}".format(self.repo.remotes.origin.push(refspec=self.repo.active_branch)[0].summary))

    def token_handler(self, nr_of_tokens):
        self._get_os_var()
        if nr_of_tokens == 1:
            self._token = os.environ.get(self._available_tokens[self.token_counter])
            self._gh = self._auth()
            if not self.limit_checker():
                self._get_reset_time()
            else:
                return True
        elif nr_of_tokens > 1:
            self._token = os.environ.get(self._available_tokens[self.token_counter])
            print(os.environ.get(self._available_tokens[self.token_counter]))
            self._gh = self._auth()
            if not self.limit_checker():
                # return True if token switch successful and credit limit was reset
                if self._switch_token():
                    return True
                else:
                    self._get_reset_time()
            else:
                return True
        else:
            self.LOGGER.critical("Missing git authentication")
            exit(9)

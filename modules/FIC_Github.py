# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3
from modules.FIC_Logger import FICLogger
from git import Repo
from git import GitError


class FICGithub(FICLogger):
    def __init__(self):
        FICLogger.__init__(self)
        from modules.config import GIT_TOKEN
        import os
        self._token = os.environ.get(GIT_TOKEN)
        self._gh = self._auth()
        self.repo_data = None
        self.repo = Repo("..")

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self, team_name, repo_name):
        return self._init_github(self._gh, team_name, repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def pull(self):
        try:
            self.LOGGER.info("pulling changes from %s", self.repo)
            pull_info = self.repo.remotes.origin.pull(refspec=self.repo.active_branch)
            self.LOGGER.info("Summary of pull: {}".format(pull_info[0]))
        except GitError:
            self.LOGGER.info("Error pulling the dates")
            exit(3)

    def add(self):
        try:
            from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
            for file in [CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH]:
                self.repo.git.add(file, update=True)
                if not self.repo.index.diff("HEAD"):
                    self.LOGGER.info("Nothing staged for commit. has the data or files changed?")
        except GitError:
            self.LOGGER.info("Failed to add the files")

    #
    # def _commit(self):
    #     # Add the commit msg.
    #     pass
    #
    # def push(self):
    #     self._add()
    #     self._commit()
    #     # Do the push
    #     pass


a = FICGithub()
a.add()

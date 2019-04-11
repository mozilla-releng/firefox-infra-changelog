# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import github3


class FICGithub:
    def __init__(self):
        from modules.config import GIT_TOKEN
        import os
        self._token = os.environ.get(GIT_TOKEN)
        self._gh = self._auth()
        self.repo_data = None

    def _auth(self):
        return github3.login(token=self._token)

    def read_repo(self, team_name, repo_name):
        return self._init_github(self._gh, team_name, repo_name)

    def _init_github(self, *args):
        self.repo_data = github3.GitHub.repository(args[0], args[1], args[2])
        return self.repo_data

    def _add(self):
        from modules.config import CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, CHANGELOG_REPO_PATH
        # Defines which files to add.
        # ./data/*
        # ./changelog.json
        # ./changelog.md
        pass

    def _commit(self):
        # Add the commit msg.
        pass

    def push(self):
        self._add()
        self._commit()
        # Do the push
        pass

    def pull(self):
        pass

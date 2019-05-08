# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class FICDataVault:
    def __init__(self):
        # Common Data
        self.uid = int()  # Used to find the object.
        self.repos_container = dict()

        # Commit Specific Data
        # Common Git and HG values
        self.commit_type          = None  # Can be "git" or "hg"
        self.commit_number        = None
        self.commit_sha           = None
        self.commit_url           = None
        self.commit_author        = None
        self.commit_author_email  = None
        self.commit_message       = None
        self.commit_date          = None
        self.commit_files_changed = None
        self.repo_name            = None
        self.team_name            = None

        # HG Specific values
        self.changeset_index      = None
        self.changeset            = None
        self.changeset_lander     = None
        self.hg_commits_list      = None
        self.changesets_json      = None
        self.constructed_dict     = {}

        # GIT Specific values
        self.folders_to_check     = []



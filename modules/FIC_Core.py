import json

from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_Logger import FICLogger
from plugins.FIC_Markdown import FICMarkdownGenerator
from modules.config import CHANGELOG_REPO_PATH, CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, DEFAULT_DAYS, REPOSITORIES_FILE
from modules.FIC_Utilities import return_time


class FICCore(FICGithub, FICMercurial, FICMarkdownGenerator, FICLogger):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICMarkdownGenerator.__init__(self)
        FICLogger.__init__(self)
        self.check_tool_integrity()

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, days=DEFAULT_DAYS, logging=False):
        # Don't forget about days!
        if all:
            # Needs to be replaced with whatever we want the script to do.
            # In this case, with a method that should run the script in all modes.
            self.LOGGER.debug("Run all behavior mode")
            self._run_all_behavior()

        if git_only:
            self.LOGGER.debug("Run Github mode")
            self._run_git_behavior()

        if hg_only:
            self.LOGGER.debug("Run Mercurial mode")
            self._run_hg_behavior()

        if repo_list:
            self.LOGGER.debug("Run repo list mode")
            self._run_custom_repos_behavior(repo_list)

        self.populate_changelog_json(days)
        self.create_changelog_md()

    def _run_all_behavior(self):
        # Describes the behavioral of the script that runs in all mode.
        for hosting_service in json.load(self.load(None, REPOSITORIES_FILE)):
            for repo in json.load(self.load(None, REPOSITORIES_FILE)).get(hosting_service):
                self.LOGGER.debug("{} working on repo: {}".format(hosting_service, repo))
                if hosting_service == "Github":
                    self.start_git(repo)
                    self.start_md_for_git(repo)
                else:
                    self.start_hg(repo)
                    self.start_md_for_hg(repo)

    def _run_git_behavior(self):
        # Describes the behavioral of the script that runs in git only mode.
        for repo in json.load(self.load(None, REPOSITORIES_FILE)).get("Github"):
            self.LOGGER.debug("{} working on repo: {}".format("Github", repo))
            self.start_git(repo)
            self.start_md_for_git(repo)

    def _run_hg_behavior(self):
        # Describes the behavioral of the script that runs in hg only mode.
        for repo in json.load(self.load(None, REPOSITORIES_FILE)).get("Mercurial"):
            self.LOGGER.debug("{} working on repo: {}".format("Mercurial", repo))
            self.start_hg(repo)
            self.start_md_for_hg(repo)

    def _run_custom_repos_behavior(self, user_repos):
        # Describes the behavioral of the script that runs with custom repos mode.
        for repo in user_repos:
            self.LOGGER.debug("{} working on repo: {}".format(repo[1], repo[0]))
            if repo[1] == "Github":
                self.start_git(repo[0])
                self.start_md_for_git(repo[0])
            elif repo[1] == "Mercurial":
                self.start_hg(repo[0])
                self.start_md_for_hg(repo[0])
            else:
                self.LOGGER.critical(f"Unknown repository type. Got {repo[1]} but can only accept 'Github' or 'Mercurial'")
                exit(12)

    def _extract_git_commits(self, key, changelog, number_of_days):
        repo_data = json.load(self.load(CHANGELOG_REPO_PATH, key.lower() + ".json"))
        if len(repo_data) > 0:
            repo_data.pop("0")
            changelog["Github"].update({key: {}})
            commit_number = 0
            for value in repo_data.values():
                time_span = return_time("%Y-%m-%dT%H:%M:%S.%f", "sub", number_of_days)
                if value["date"] > time_span:
                    changelog["Github"][key].update({commit_number: value})
                    commit_number += 1

    def _extract_hg_commits(self, key, changelog, number_of_days):
        repo_data = json.load(self.load(CHANGELOG_REPO_PATH, key.lower() + ".json"))
        if len(repo_data) > 0:
            repo_data.pop("0")
            changelog["Mercurial"].update({key: {}})
            commit_number = 0
            for value in repo_data.values():
                time_span = return_time("%Y-%m-%dT%H:%M:%S.%f", "sub", number_of_days)
                if value["date_of_push"] > time_span:
                    changelog["Mercurial"][key].update({commit_number: value})
                    commit_number += 1

    def populate_changelog_json(self, number_of_days):
        changelog = {}
        changelog.update({"Github": {},
                          "Mercurial": {}})
        with open(self.construct_path(None, REPOSITORIES_FILE), "r") as json_data:
            local_data = json.load(json_data)
            # Check all Github files exist for each repository.
            for key in local_data["Github"].keys():
                self._extract_git_commits(key, changelog, number_of_days)
            for key in local_data["Mercurial"].keys():
                self._extract_hg_commits(key, changelog, number_of_days)
        self.save(None, CHANGELOG_JSON_PATH, changelog)

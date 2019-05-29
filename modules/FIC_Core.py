import json

from modules.FIC_Github import FICGithub
from modules.FIC_Mercurial import FICMercurial
from modules.FIC_FileHandler import FICFileHandler
from modules.FIC_Logger import FICLogger
from plugins.FIC_Markdown import FICMarkdownGenerator
from modules.config import CHANGELOG_REPO_PATH, CHANGELOG_JSON_PATH, CHANGELOG_MD_PATH, DEFAULT_DAYS
from modules.FIC_Utilities import return_time


class FICCore(FICGithub, FICMercurial, FICFileHandler, FICLogger, FICMarkdownGenerator):
    def __init__(self):
        FICGithub.__init__(self)
        FICMercurial.__init__(self)
        FICFileHandler.__init__(self)
        FICLogger.__init__(self)
        FICMarkdownGenerator.__init__(self)
        self.check_tool_integrity()

    def run_fic(self, all=False, git_only=False, hg_only=False, repo_list=None, days=3, logging=False, user_repos=None):
        # Don't forget about days!
        if all:
            # Needs to be replaced with whatever we want the script to do.
            # In this case, with a method that should run the script in all modes.
            print("Changelog has run in All mode!")
            self._run_all_behavior()

        if git_only:
            print("Changelog has run in git only mode!")
            self._run_git_behavior()

        if hg_only:
            print("Changelog has run in hg only mode!")
            self._run_hg_behavior()

        if repo_list:
            print("Changelog has run with a custom list of repositories!")
            self._run_custom_repos_behavior(user_repos)

    def _markdown_iterator(self):
        _json_data = json.load(self.load(None, "repositories.json"))
        for hosting_service in _json_data:
            for repo in _json_data.get(hosting_service):
                if hosting_service == "Github":
                    self.start_md_for_git(repo)
                else:
                    self.start_md_for_hg(repo)

    def _run_all_behavior(self):
        # Describes the behavioral of the script that runs in all mode.
        print("Testing run all behavioral...")

        for hosting_service in json.load(self.load(None, "repositories.json")):
            for repo in json.load(self.load(None, "repositories.json")).get(hosting_service):
                if hosting_service == "Github":
                    self.start_git(repo)
                else:
                    self.start_hg(repo)

    def _run_git_behavior(self):
        # Describes the behavioral of the script that runs in git only mode.
        print("Testing git mode behavioral...")

        for repo in json.load(self.load(None, "repositories.json")).get("Github"):
            self.start_git(repo)

    def _run_hg_behavior(self):
        # Describes the behavioral of the script that runs in hg only mode.
        print("Testing hg mode behavioral...")

        for repo in json.load(self.load(None, "repositories.json")).get("Mercurial"):
            self.start_hg(repo)

    def _run_custom_repos_behavior(self, user_repos):
        # Describes the behavioral of the script that runs with custom repos mode.
        print("Testing custom repositories mode behavioral...")

        for repo in user_repos:
            if repo[1] == "Github":
                self.start_git(repo)
            elif repo[1] == "Mercurial":
                self.start_hg(repo)
            else:
                self.LOGGER.critical(f"Unknown repository type. Got {repo[1]} but can only accept 'Github' or 'Mercurial'")
                exit(12)

    def _extract_git_commits(self, key, changelog, number_of_days):
        repo_data = json.load(self.load(CHANGELOG_REPO_PATH, key.lower() + ".json"))
        if len(repo_data) > 1:
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
        if len(repo_data) > 1:
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
        with open(self.construct_path(None, "repositories.json"), "r") as json_data:
            local_data = json.load(json_data)
            # Check all Github files exist for each repository.
            for key in local_data["Github"].keys():
                self._extract_git_commits(key, changelog, number_of_days)
            for key in local_data["Mercurial"].keys():
                self._extract_hg_commits(key, changelog, number_of_days)
        self.save(None, CHANGELOG_JSON_PATH, changelog)

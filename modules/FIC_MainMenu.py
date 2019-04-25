# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import sys
import json
from modules.FIC_FileHandler import FICFileHandler


class FICMainMenu(FICFileHandler):
    def __init__(self):
        import argparse
        FICFileHandler.__init__(self)
        self.logging = False
        self.git_only = False
        self.hg_only = False
        self.all = False
        self.repo = False
        self.days = False
        self.push = False
        self.parser = argparse.ArgumentParser()
        self.choice = int
        self.repository_list = []
        self.directory = "../"  # Hardcoded for now. We will need to pass this dynamically.

    def parse_arguments(self):
        self.parser.add_argument('-a', '--all', required=False, action='store_true', default=False,
                                 help='Runs script for all available repositories')
        self.parser.add_argument('-g', '--git', required=False, action='store_true', default=False,
                                 help='Runs script only for repos that are on GitHub')
        self.parser.add_argument('-hg', '--mercurial', required=False, action='store_true', default=False,
                                 help='Runs script only for repos that are on Mercurial')
        self.parser.add_argument("-r", "--repo", required=False, action='store_true', default=False,
                                 help="Let the user choose for which repositories the script will run")
        self.parser.add_argument("-l", "--logging", required=False, action='store_true', default=False,
                                 help="Activate logger output in the console")
        self.parser.add_argument("-d", "--days", required=False, action='store', default=3,
                                 help="Generate the changelog.md for <int> amount of days.")
        self.parser.add_argument("-p", "--push", required=False, action='store_true', default=False,
                                 help="Runs script for all available repositories and auto push the changes to github")
        args = self.parser.parse_args()
        return args

    def _set_argument_flags(self, args):
        if args.logging:
            self.logging = True

        if args.git:
            self.git_only = True

        if args.mercurial:
            self.hg_only = True

        if args.all:
            self.all = True

        if args.repo:
            self.repo = True

        if args.days:
            if str(args.days).isdecimal():
                self.days = int(args.days)
            else:
                print("When using -d/--days please insert a number of days.\n"
                      "Example: python3 client.py -d 30 or --days 10")
                exit(4)

        if args.push:
            self.push = True
        return

    def _choice_main_menu(self):
        if self.choice is 1:
            self.all = True
            self._check_arguments_state()

        if self.choice is 2:
            self.git_only = True
            self._check_arguments_state()

        if self.choice is 3:
            self.hg_only = True
            self._check_arguments_state()

        if self.choice is 4:
            self.repo = True
            self._check_arguments_state()

        if self.choice is 5:
            self.logging = True
            self.main_menu()

        if self.choice is 6:
            days_choice = input("Please enter the number of days you want changelog.md to be generated for\n")
            if str(days_choice).isdecimal():
                self.days = days_choice
            else:
                print("When using option 6 please use integers only.")
                exit(4)
            self.main_menu()

        if self.choice is 7:
            self.push = True
            self.main_menu()  # Placeholder.
        return

    def repo_selection_menu(self):
        new_list = []
        while input != "q":
            print("You have selected : ", new_list)
            for keys in self.repository_list:
                print(self.repository_list.index(keys) + 1, keys)

            user_choice = input("Select a repo by typing it's "
                                "number, "
                                "type q when you are done: ")
            if str(user_choice) == "q":
                for repository in new_list:
                    if repository in self.load_repositories.get("Github"):
                        # Place holder for generating json/md files for git
                        pass
                    elif repository in self.load_repositories.get("Mercurial"):
                        # Place holder for generating json/md files for hg
                        pass
            try:
                new_entry = int(user_choice) - 1
                if new_entry < 0 or new_entry >= len(self.repository_list):
                    print('Choice not valid. Please provide a choice according to the list printed below!')
                else:
                    new_list.append(self.repository_list[int(new_entry)])
                    self.repository_list.pop(int(new_entry))
            except ValueError:
                exit(11)

    def main_menu(self):
        self._check_arguments_state()
        if len(sys.argv) == 1:
            print("Welcome to Ciduty's Firefox Infra Changelog!\n"
                  "You can use the options below to run the script according to your needs.\n"
                  "\n"
                  "1. Run script for all available repositories \n"
                  "2. Run script only for repositories that are on GitHub\n"
                  "3. Run script only for repositories that are on Mercurial\n"
                  "4. Run script only for repositories that are chosen by you (Both GitHub and/or Mercurial)\n"
                  "5. Activates logger output in console\n"
                  "6. Generates changelog.md for the amount of days set by user\n"
                  "7. Run the script for all available repositories and pushes .json/.md changes to Git\n"
                  "0. Exit application.")
            self.choice = int(input())
            self._choice_main_menu()
            return
        else:
            self._set_argument_flags(self.parse_arguments())  # Set all flags before showing the menu.
            self._check_arguments_state()

    def _check_arguments_state(self):
        if self.logging:
            print("==== Logging is active ====")

        if self.git_only:
            print("==== Running in GIT only mode ====")

        if self.hg_only:
            print("==== Running in MERCURIAL only mode ====")

        if self.all:
            print("==== Running in ALL repositories mode ====")

        if self.push:
            print("==== Running in ALL repositories and pushing to Github ====")

        if self.repo:
            self.construct_repository_list()
            self.repo_selection_menu()

    def _load_repository_data(self, directory):
        self.load_repositories = json.load(self.load(directory, "repositories.json"))
        return self.load_repositories

    def construct_repository_list(self):
        self._load_repository_data("../")
        for key in self.load_repositories:
            for repository_name in self.load_repositories.get(key):
                self.repository_list.append(repository_name)
        return self.repository_list


if __name__ == "__main__":
    testing_arguments = FICMainMenu()
    testing_arguments.main_menu()

    print("Logging       :", testing_arguments.logging)
    print("Git Only      :", testing_arguments.git_only)
    print("HG Only       :", testing_arguments.hg_only)
    print("All           :", testing_arguments.all)
    print("Repo Selection:", testing_arguments.repo)
    print("Push to Github:", testing_arguments.push)
    print("Number of Days:", testing_arguments.days)
    print("Choice        :", testing_arguments.choice)

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import sys
import json
import argparse
from modules.FIC_Core import FICCore

from modules.config import DEFAULT_DAYS, REPOSITORIES_FILE


class FICMainMenu(FICCore):
    def __init__(self):
        FICCore.__init__(self)
        self.all = False
        self.git_only = False
        self.hg_only = False
        self.repo_selection = False
        self.logging = False
        self.days = DEFAULT_DAYS
        self.push = False
        self.dev = False
        self.skip_menu = False
        self.parser = argparse.ArgumentParser()
        self.arguments_set = False  # Check to see if we set the Flag values or not. Helps to skip un-needed iterations.

    def start(self):
        # Set all argument flags, based on runtime arguments.
        self._available_arguments()

        # Check if we want to skip the menu or not.
        if not self.skip_menu:
            self._main_menu()

        # Skip the menu.
        else:
            # TODO: Add ability to skip every menu. Not only ALL
            # Check if we ONLY typed `python client.py -s/--skip-menu`
            # If check is True, set self.all = True then run FIC main logic.
            # We don't need to check if "-s/--skip-menu" is present, as this is the only way to
            # enter this else statement.
            self.all = True if len(sys.argv) <= 2 else self.all

            self.run_fic(all=self.all,
                         git_only=self.git_only,
                         hg_only=self.hg_only,
                         days=self.days,
                         logging=self.logging)

    def _available_arguments(self):
        self.parser.add_argument('-a', '--all', required=False, action='store_true', default=False,
                                 help='Runs script for all available repositories')
        self.parser.add_argument('-g', '--git', required=False, action='store_true', default=False,
                                 help='Runs script only for repos that are on GitHub')
        self.parser.add_argument('-hg', '--mercurial', required=False, action='store_true', default=False,
                                 help='Runs script only for repos that are on Mercurial')
        self.parser.add_argument("-r", "--repo", required=False, nargs="*",
                                 help="Let the user choose for which repositories to run")
        self.parser.add_argument("-l", "--logging", required=False, action='store_true', default=False,
                                 help="Activate logger output in the console")
        self.parser.add_argument("-days", "--days", required=False, action='store', default=DEFAULT_DAYS,
                                 help="Generate the changelog.md for <int> amount of days.")
        self.parser.add_argument("-p", "--push", required=False, action='store_true', default=False,
                                 help="Runs for all available repositories and auto-push to github")
        self.parser.add_argument("-dev", "--development", required=False, action='store_true', default=False,
                                 help="Activate development mode")
        self.parser.add_argument("-s", "--skip-menu", required=False, action="store_true", default=False,
                                 help="Skip MainMenu. Used for automatization.")

        self.args = self.parser.parse_args()
        self._set_arguments_flags()

    def _set_arguments_flags(self):
        # Check that we have parsed all arguments.
        if not self.args:
            self._available_arguments()
        else:
            pass

        # Create and set flags.
        if self.args.all:
            self.all = True

        if self.args.git:
            self.git_only = True

        if self.args.mercurial:
            self.hg_only = True

        # Check if Manual Repo Selection is present and in which mode:
        #   - If `-r` is missing.                                 (Return: False)
        #   - If `-r` is present, but no list present.            (Return: True)
        #   - If `-r` is present and a list of repos are present. (Return: List of repos)
        repo_selection = False if isinstance(self.args.repo, type(None)) else self.args.repo
        if repo_selection:
            self.repo_selection = self.args.repo

        if self.args.logging:
            self.logging = True

        if self.args.days:
            if str(self.args.days).isdecimal():
                self.days = int(self.args.days)
            else:
                print("When using -d/--days please insert a number of days.\n"
                      "Example: python3 client.py -d 30 or --days 10")
                exit(4)

        if self.args.push:
            self.push = True

        if self.args.development:
            self.dev = True

        if self.args.skip_menu:
            self.skip_menu = True

        self.arguments_set = True

    def _construct_mainmenu_text(self):
        if not self.arguments_set:
            self._set_arguments_flags()
        else:
            pass

        menu_header = "Welcome to Ciduty's Firefox Infra Changelog!\n" \
                      "You can use the options below to run the script according to your needs.\n"

        menu_logging = "====        Logging  is active        ====\n"
        menu_dev     = "====        Dev Mode is active        ====\n"
        menu_days    = f"==== Generating Changelog for {self.days} days  ====\n"

        menu_notifications = (menu_logging if self.logging else "") + \
                             (menu_dev if self.dev else "") + \
                             (menu_days if self.days is not DEFAULT_DAYS else "")

        menu_options = "1. Run script for all available repositories \n" \
                       "2. Run script only for repositories that are on GitHub\n" \
                       "3. Run script only for repositories that are on Mercurial\n" \
                       "4. Run script for repositories that you choose\n" \
                       "5. Activates logger output in console\n" \
                       "6. Generates changelog.md for the amount of days set by user\n" \
                       "7. Run the script for all repositories and push changes to Github\n" \
                       "0. Exit application."

        return menu_header + menu_notifications + menu_options

    def _main_menu(self):
        print(self._construct_mainmenu_text())
        self.choice = int(input())
        self._run_selected_menu(choice=self.choice)

    def _run_selected_menu(self, choice):
        if choice == 1:
            self.LOGGER.info(f"Script running for choice {choice}: ALL Repositories.")
            self.run_fic(all=True,
                         logging=self.logging,
                         days=self)

        if choice == 2:
            self.LOGGER.info(f"Script running for choice {choice}: Git Repositories Only.")
            self.run_fic(git_only=True,
                         logging=self.logging,
                         days=self)

        if choice == 3:
            self.LOGGER.info(f"Script running for choice {choice}: HG Repositories Only.")
            self.run_fic(hg_only=True,
                         logging=self.logging,
                         days=self)

        if choice == 4:
            self.LOGGER.info(f"Script running for choice {choice}: Custom Repositories.")
            self._repo_selection_menu()
            self.run_fic(repo_list=self.repo_selection)

        if choice == 5:
            self.logging = not self.logging
            if self.logging:
                self.LOGGER.info("Console Logging has been activated.")
            else:
                self.LOGGER.info("Console Logging has been deactivated.")
            self._main_menu()

        if choice == 6:
            print("Please input the amount of days `changelog.md` will be generated for:")
            days = input()

            if str(days).isdecimal():
                self.days = int(days)
                self.LOGGER.info(f"DEFAULT_DAYS parameter has been changed to: {self.days} day(s)")
                self._main_menu()
            else:
                print("Amount of days need to be an integer!\n"
                      "Moving back to Main Menu.")
                self._main_menu()

        if choice == 7:
            pass

        if choice == 0:
            exit()

    def _repo_selection_menu(self):
        repo_list = json.load(self.load(None, REPOSITORIES_FILE))
        temp_list = []

        # Argument "-r" provided, but no list of repositories is included.
        # Enter Selection Menu.
        if not self.repo_selection or (len(self.repo_selection) == 0):
            self._construct_repo_selection(repo_list)

        # Argument "-r" provided and list of repositories is included.
        # Skip Selection Menu
        else:
            for key in repo_list:
                for repo in repo_list.get(key):
                    for selection in self.repo_selection:
                        if int(selection) == repo_list.get(key).get(repo).get("order"):
                            temp_list.append((int(selection), repo, key))

            self.repo_selection = []
            for _, repo, key in temp_list:
                self.repo_selection.append((repo, key))

    def _construct_repo_selection(self, repo_list):
        temp_list = []
        self.repo_selection = []
        for key in repo_list:
            for repo in repo_list.get(key):
                temp_list.append((repo_list.get(key).get(repo).get("order"), repo, key))
        print("Available Repositories:")
        for entry in sorted(temp_list):
            print(entry[0], entry[1])

        print("Enter the number of the repositorie(s) you want to run, separated by comma.\n"
              "Example: 1, 5, 20, 3, 2")
        choices = input()
        choices = choices.split(",")

        self.repo_selection = []
        for key in repo_list:
            for repo in repo_list.get(key):
                for choice in choices:
                    if int(choice) == repo_list.get(key).get(repo).get("order"):
                        self.repo_selection.append((repo, key))

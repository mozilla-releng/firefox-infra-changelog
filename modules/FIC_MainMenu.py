# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class FICMainMenu:
    def __init__(self):
        import argparse
        self.logging = False
        self.git_only = False
        self.hg_only = False
        self.all = False
        self.repo = False
        self.days = False
        self.push = False
        self.parser = argparse.ArgumentParser()

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

    def repo_selection_menu(self):
        pass

    def main_menu(self):
        self._set_argument_flags(self.parse_arguments())  # Set all flags before showing the menu.
        pass

    pass


testing_arguments = FICMainMenu()
testing_arguments.main_menu()
print("Logging       :", testing_arguments.logging)
print("Git Only      :", testing_arguments.git_only)
print("HG Only       :", testing_arguments.hg_only)
print("All           :", testing_arguments.all)
print("Repo Selection:", testing_arguments.repo)
print("Push to Github:", testing_arguments.push)
print("Number of Days:", testing_arguments.days)

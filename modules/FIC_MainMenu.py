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
        self.update = False
        self.parser = argparse.ArgumentParser()
        self.a = self.parse_arguments()

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
        self.parser.add_argument("-d", "--days", required=False, action='store_true', default=False,
                                 help="Generate the changelog.md for <int> amount of days.")
        self.parser.add_argument("-p", "--push", required=False, action='store_true', default=False,
                                 help="Runs script for all available repositories and auto push the changes to github")
        args = self.parser.parse_args()

        if args.all:
            self.all = True

        if args.logging:
            self.logging = True

        return args, self.all

    def repo_selection_menu(self):
        pass

    def main_menu(self):
        pass

    pass


testing_arguments = FICMainMenu()
print(testing_arguments.all)
print(testing_arguments.logging)
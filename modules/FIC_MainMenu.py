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

        choice = input()

        if choice == 1:
            self.all = True

        if choice == 2:
            self.git_only = True

        if choice == 3:
            self.hg_only = True

        if choice == 4:
            self.repo = True

        if choice == 5:
            self.logging = True

        if choice == 6:
            days_choice = input("Please enter the number of days you want changelog.md to be generated for\n")
            if str(days_choice).isdecimal():
                self.days = days_choice
            else:
                print("When using option 6 please use integers only.")
                exit(4)

        else:
            exit(0)

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

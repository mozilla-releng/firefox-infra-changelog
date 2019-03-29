"""
Firefox-Infra-Changelog: tool which build a
changelog of commits happening on git or hg that
could affect Firefox CI Infra
"""
import logging
from datetime import datetime
import click
import json
import subprocess
import signal
from fic_modules.FICExceptions import FICExceptions
from github import GithubException
from fic_modules.git import create_files_for_git
from fic_modules.hg import create_files_for_hg
from fic_modules.GITMethods import Github
from fic_modules.helper_functions import (
    clear_file,
    get_keys,
    write_to_changelog_json
)
from fic_modules.configuration import (
    REPO_LIST,
    REPOSITORIES,
    LOGGER
)
from fic_modules.markdown_modules import generate_main_md_table


def run_all(logger, days):
    """
    Run the script for all currently tracked repositories.
    :param logger: LOGGER object
    :param days: Number of days (int) for which FIC will generate the
    changelog.md data tables.
    """
    logger.info("======== Logging in ALL mode on %s ========", datetime
                .now())
    git_data = create_files_for_git(REPOSITORIES, onerepo=False)
    hg_data = create_files_for_hg(REPOSITORIES, onerepo=False)
    # Take git and hg data, write it to changelog.json
    changelog_data = {}
    changelog_data.update({"Github": git_data})
    changelog_data.update({"Hg": hg_data})
    data_file = open("changelog.json", "w")
    json.dump(changelog_data, data_file, indent=2)
    data_file.close()
    clear_file("changelog.md", int(days))
    generate_main_md_table(REPOSITORIES, "complete", int(days))


def update_all(logger, days):
    """
    Run the script for all currently tracked repositories.
    :param logger: LOGGER object
    :param days: Number of days (int) for which FIC will generate the
    changelog.md data tables.
    """
    config = "."
    commit_message = "Changelog: " + str(datetime.utcnow())
    files = ["git_files", "hg_files", "changelog.json", "changelog.md"]
    update_fic_files = Github(files, commit_message, LOGGER, config)
    update_fic_files.git_pull()
    logger.info("======== Logging in ALL mode on %s ========", datetime
                .now())
    git_data = create_files_for_git(REPOSITORIES, onerepo=False)
    hg_data = create_files_for_hg(REPOSITORIES, onerepo=False)
    # Take git and hg data, write it to changelog.json
    changelog_data = {}
    changelog_data.update({"Github": git_data})
    changelog_data.update({"Hg": hg_data})
    data_file = open("changelog.json", "w")
    json.dump(changelog_data, data_file, indent=2)
    data_file.close()
    clear_file("changelog.md", int(days))
    generate_main_md_table(REPOSITORIES, "complete", int(days))
    update_fic_files.git_add()
    update_fic_files.git_commit()
    update_fic_files.git_push()


def run_git(logger, days):
    """
    Run the script only for GIT repositories that are currently tracked.
    :param logger: LOGGER object
    :param days: Number of days (int) for which FIC will generate the
    changelog.md data tables.
    """
    logger.info("======== Logging in GIT mode on %s ========", datetime
                .now())
    git_data = create_files_for_git(REPOSITORIES, onerepo=False)
    repo_name = "Github"
    write_to_changelog_json(git_data, repo_name)
    clear_file("changelog.md", int(days))
    generate_main_md_table(REPOSITORIES, "Git", int(days))
    click.echo("Script ran in GIT Only mode")


def run_hg(logger, days):
    """
    Run the script only for HG repositories that are currently tracked.
    :param logger: LOGGER object
    :param days: Number of days (int) for which FIC will generate the
    changelog.md data tables.
    """
    logger.info("======== Logging in HG mode on %s ========", datetime
                .now())
    hg_data = create_files_for_hg(REPOSITORIES, onerepo=False)
    repo_name = "Hg"
    write_to_changelog_json(hg_data, repo_name)
    clear_file("changelog.md", int(days))
    generate_main_md_table(REPOSITORIES, "Hg", int(days))
    click.echo("Script ran in HG Only mode")


def run_multiple(logger, days):
    """
    Manually specify for which repositories you want to update the data.
    :param logger: LOGGER object
    :param days: Number of days (int) for which FIC will generate the
    changelog.md data tables.
    """
    get_keys("Github")
    get_keys("Mercurial")
    new_list = []
    while input != "q":
        print("You have selected : ", new_list)
        for keys in REPO_LIST:
            print(REPO_LIST.index(keys) + 1, keys)

        user_choice = input("Select a repo by typing it's "
                            "number, "
                            "type q when you are done: ")
        if str(user_choice) == "q":
            logger.info('========Logging for %s on %s ========'
                        , str(new_list).strip('[]'), datetime
                        .now())
            for repository in new_list:
                if repository in REPOSITORIES.get("Github"):
                    create_files_for_git(repository, onerepo=True)
                    generate_main_md_table(REPOSITORIES, "complete", int(days))
                elif repository in REPOSITORIES.get("Mercurial"):
                    create_files_for_hg(repository, onerepo=True)
                    clear_file("changelog.md", int(days))
                    generate_main_md_table(REPOSITORIES, "complete", int(days))
        try:
            new_entry = int(user_choice) - 1
            if new_entry < 0 or new_entry >= len(REPO_LIST):
                print('Choice not valid!')
            else:
                new_list.append(REPO_LIST[int(new_entry)])
                REPO_LIST.pop(int(new_entry))
        except ValueError:
            exit(0)


def run_days(logger, days):
    """
    Simple logger utility to track how many days we will generate data for.
    """
    logger.info('Generating changelog for %s days', days)


@click.command()
@click.option('-g', '--git', is_flag=True, flag_value='git',
              help='Run only for GIT repos')
@click.option('-hg', '--mercurial', is_flag=True, flag_value='mercurial',
              help='Run only for HG repos')
@click.option('-l', '--logger', is_flag=True, flag_value='logger',
              help='Display logger')
@click.option('-m', '--manual', is_flag=True, flag_value='manual',
              help='Let you choose for which repositories the script will run')
@click.option('-c', '--complete', is_flag=True, flag_value='complete',
              help='Run for all currently available repositories')
@click.option('-d', '--days', default=3, help='Let user decide for how many '
                                              'days changelog.md will '
                                              'be generated')
@click.option('-u', '--update', is_flag=True, help='Automatically push the updated'
                                                   'data to github.')
@click.help_option('-h', '--help')
def cli(complete=False, git=False, mercurial=False, logger=False, manual=False,
        days=False, update=False):
    """
    Main function of the script that handles how the script runs
    :param update: push the new changes to Github
    :param complete: Used to run the script for all of the repositories.
    :param git: Used to run the script in git mode only
    :param mercurial: Used to run the script in mercurial mode only
    :param logger: used for displaying the logger while running the script
    manually from terminal.
    :param manual: Used for running the script for specific repositories.
    :param days: Used to change the amount of days the changelog will be
    generated for
    """
    valid_args = ['-d', '--days', '-g', '--git', '-h', '--mercurial', '-l',
                  '--logger', '-m', '--manual', '-c', '--complete', '-u', '--update']
    run_arguments = list(click.get_current_context().args)
    len_args = 0
    list_args = []
    for arg in run_arguments:
        if arg not in valid_args:
            len_args += 1
            list_args.append(arg)
    if len(list_args) >= 1:
        print("The following Arguments " + str(
            list_args) + " are not available.\n"
                         "Please type python client.py -h for a list of"
                         " available arguments.")
    from fic_modules.configuration import LOGGER
    if days:
        run_days(LOGGER, days)
    if logger:
        logging.getLogger().addHandler(logging.StreamHandler())
    if complete:
        run_all(LOGGER, days)
    if git:
        run_git(LOGGER, days)
    if mercurial:
        run_hg(LOGGER, days)
    if manual:
        run_multiple(LOGGER, days)
    if update:
        update_all(LOGGER, days)


def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    subprocess.call(['git', 'checkout', 'git_files/', 'hg_files/',
                     'changelog.md', 'changelog.json'])
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    try:
        cli()
    except GithubException as error_code:
        FICExceptions(error_code.status).handle_exception()

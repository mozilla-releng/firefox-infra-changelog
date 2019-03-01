"""
Firefox-Infra-Changelog: tool which build a
changelog of commits happening on git or hg that
could affect Firefox CI Infra
"""
import logging
from datetime import datetime
import click
from fic_modules.git import create_files_for_git
from fic_modules.hg import create_files_for_hg
from fic_modules.helper_functions import (
    clear_file,
    get_keys
)
from fic_modules.configuration import (
    REPO_LIST,
    GENERATE_FOR_X_DAYS,
    REPOSITORIES
)
from fic_modules.markdown_modules import generate_main_md_table


def run_all(logger):
    logger.info("======== Logging in ALL mode on %s ========", datetime
                .now())
    create_files_for_git(REPOSITORIES, onerepo=False)
    create_files_for_hg(REPOSITORIES, onerepo=False)
    clear_file("changelog.md", GENERATE_FOR_X_DAYS)
    generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
    generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)


def run_git(logger):
    logger.info("======== Logging in GIT mode on %s ========", datetime
                .now())
    create_files_for_git(REPOSITORIES, onerepo=False)
    clear_file("changelog.md", GENERATE_FOR_X_DAYS)
    generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
    generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
    click.echo("Script ran in GIT Only mode")


def run_hg(logger):
    logger.info("======== Logging in HG mode on %s ========", datetime
                .now())
    create_files_for_hg(REPOSITORIES, onerepo=False)
    clear_file("changelog.md", GENERATE_FOR_X_DAYS)
    generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
    generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
    click.echo("Script ran in HG Only mode")


def run_multiple(logger):
    get_keys("Github")
    get_keys("Mercurial")
    for scriptrepo in REPOSITORIES.get("Github").get("build-puppet") \
            .get("configuration").get("files-to-check"):
        REPO_LIST.append(scriptrepo)
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
                    generate_main_md_table("git_files",
                                           GENERATE_FOR_X_DAYS)
                elif repository in REPOSITORIES.get("Mercurial"):
                    create_files_for_hg(repository, onerepo=True)
                    clear_file("changelog.md",
                               GENERATE_FOR_X_DAYS)
                    generate_main_md_table("hg_files",
                                           GENERATE_FOR_X_DAYS)
                    generate_main_md_table("git_files",
                                           GENERATE_FOR_X_DAYS)
        try:
            new_entry = int(user_choice) - 1
            if new_entry < 0 or new_entry >= len(REPO_LIST):
                print('Choice not valid!')
            else:
                new_list.append(REPO_LIST[int(new_entry)])
                REPO_LIST.pop(int(new_entry))
        except ValueError:
            exit(0)


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
@click.help_option('-h', '--help')
def cli(complete=False, git=False, mercurial=False, logger=False, manual=False):
    """
    Main function of the script that handles how the script runs
    :param complete: Used to run the script for all of the repositories.
    :param git: Used to run the script in git mode only
    :param mercurial: Used to run the script in mercurial mode only
    :param logger: used for displaying the logger while running the script
    manually from terminal.
    :param manual: Used for running the script for specific repositories.
    :return:
    """
    from fic_modules.configuration import LOGGER

    if logger:
        logging.getLogger().addHandler(logging.StreamHandler())
    if complete:
        run_all(LOGGER)
    if git:
        run_git(LOGGER)
    if mercurial:
        run_hg(LOGGER)
    if manual:
        run_multiple(LOGGER)


if __name__ == "__main__":
    cli()

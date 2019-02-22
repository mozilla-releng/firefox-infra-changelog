import click
import logging
from datetime import datetime
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


@click.group()
def cli():
    """Firefox-Infra-Changelog: tool which build a
    changelog of commits happening on git or hg that
    could affect Firefox CI Infra"""
    pass


@cli.command()
@click.option('--all', flag_value='a',
              help='Run for all currently available repositories')
@click.option('--git', is_flag=True, flag_value='git', help='Run only for GIT'
                                                            'repos')
@click.option('--hg', is_flag=True, flag_value='hg', help='Run only for HG'
                                                          ' repos')
@click.option('--l', is_flag=True, flag_value='l', help='Display logger')
@click.option('--m', is_flag=True, flag_value='m',
              help='Let you choose for which repositories the script will run')
def cli(all, git, hg, l, m):
    from fic_modules.configuration import LOGGER
    """
    Firefox-Infra-Changelog: tool which build a
    changelog of commits happening on git or hg that
    could affect Firefox CI Infra"""
    if l:
        logging.getLogger().addHandler(logging.StreamHandler())
    if all:
        LOGGER.info("========Logging in ALL mode on {}========"
                    .format(datetime.now()))
        create_files_for_git(REPOSITORIES, onerepo=False)
        create_files_for_hg(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
    if git:
        LOGGER.info("========Logging in GIT mode on {}========"
                    .format(datetime.now()))
        create_files_for_git(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
        click.echo("Script ran in GIT Only mode")
    if hg:
        LOGGER.info("========Logging in HG mode on {} ========"
                    .format(datetime.now()))
        create_files_for_hg(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
        click.echo("Script ran in HG Only mode")
    if m:
        get_keys("Github")
        get_keys("Mercurial")
        for scriptrepo in REPOSITORIES.get("Github").get("build-puppet")\
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
                LOGGER.info('========Logging for {} on {} ========'
                            .format(str(new_list).strip('[]'), datetime
                                    .now()))
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
                    print('Not Valid')
                else:
                    new_list.append(REPO_LIST[int(new_entry)])
                    REPO_LIST.pop(int(new_entry))
            except ValueError:
                exit(0)


if __name__ == "__main__":
    cli()


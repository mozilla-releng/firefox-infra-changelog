import click
from git import create_files_for_git
from hg import create_files_for_hg
from fic_modules.helper_functions import (
    clear_file,
    get_keys
)
from fic_modules.configuration import (
    REPO_LIST,
    GENERATE_FOR_X_DAYS,
    REPOSITORIES
)
from markdown_modules import generate_main_md_table


@click.command()
@click.option('--git', flag_value='git', help='Run script only for GIT repos')
@click.option('--hg', flag_value='hg', help='Run script only for HG repos')
@click.option('--l', flag_value='l', help='Display logger')
@click.option('--r', flag_value='r',
              help='Let you choose for which repositories the script will run')

def cli(git, hg, l, r):
    """

    :param git: Runs the script only for GIT repositories
    :param hg: Runs the script only for HG repositories
    :param l: Display logger
    :param r: Let you choose for which repositories the script will run
    :param d: Let you choose the amount of days the main markdown file will
    contain
    :return:
    """

    if git:
        create_files_for_git(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
        click.echo("Script ran in GIT Only mode")
    if hg:
        create_files_for_hg(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)
        click.echo("Script ran in HG Only mode")
    if l:
        logger = True
    if r:
        get_keys("Github")
        get_keys("Mercurial")
        # for scriptrepo in repositories.get("Github").get("build-puppet").get("configuration").get("files-to-check"):
        #     repoList.append(scriptrepo)
        new_list = []
        while input != "q":
            print("You have selected : ", new_list)
            for keys in REPO_LIST:
                print(REPO_LIST.index(keys) + 1, keys)

            user_choice = input("Select a repo by typing it's "
                                "number, "
                                "type q when you are done: ")
            if str(user_choice) == "q":
                print('Running script for {}'
                      .format(str(new_list).strip('[]')))
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

    else:
        create_files_for_git(REPOSITORIES, onerepo=False)
        create_files_for_hg(REPOSITORIES, onerepo=False)
        clear_file("changelog.md", GENERATE_FOR_X_DAYS)
        generate_main_md_table("hg_files", GENERATE_FOR_X_DAYS)
        generate_main_md_table("git_files", GENERATE_FOR_X_DAYS)


if __name__ == "__main__":
    cli()



"""
This module handles the mercurial generation, filtering and other mercurial
related stuff.
"""
import json
from datetime import (
    datetime,
    timedelta
)
import time
import requests
from fic_modules.configuration import (
    REPOSITORIES,
    WORKING_DIR,
    NUMBER_OF_CHANGESETS,
    LOGGER
)
from fic_modules.helper_functions import (
    remove_chars,
    compare_files,
    extract_reviewer,
    replace_bug_with_url,
    populate_changelog_json
)


def get_last_local_push_id(repo_name):
    """
    :param repo_name: name of the repo we are currently working on
    :return: last_stored_push_id: last push id that is currently stored locally
    """
    hg_json_filename = "{}.json".format(repo_name)
    try:
        with open(WORKING_DIR + "/hg_files/" + hg_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
        last_stored_push_id = json_content.get("0").get("last_push_id")
        LOGGER.info("Last local push id is: %s", last_stored_push_id)
    except FileNotFoundError:
        last_stored_push_id = 0
        LOGGER.info("No last local push id found, starting from 0 ")
    return last_stored_push_id


def generate_hg_pushes_link(repo_name, repository_url):
    """
    :param repo_name: name of the repo we are currently working on
    :param repository_url: base repository url stored in repositories.json
    :return: generate_pushes_link: a link used for bringing data from HG
    """
    start_id = get_last_local_push_id(repo_name)
    url = repository_url + "json-pushes?version=2"
    response = requests.get(url).text
    data = json.loads(response)
    end_id = data.get("lastpushid")
    if start_id == 0:
        start_id = end_id - NUMBER_OF_CHANGESETS
        if end_id < 100:
            start_id = 1
    start_id = str(start_id)
    end_id = str(end_id)
    generate_pushes_link = repository_url + "json-pushes?version=2&" \
                                            "full=1&startID={}&endID={}" \
                                            .format(start_id, end_id)
    LOGGER.info("Generated link for %s is %s", repo_name, generate_pushes_link)
    return generate_pushes_link


def create_files_for_hg(repositories_holder, onerepo):
    """
    Main HG function.
    Takes every Mercurial repo from a .json file which is populated with
    repositories and writes all the commit data of each repo in a.
    creates a json and MD file for each repo as well.
    :param: repositories_holder: Expects a .json file that contains a list of
    repositories
    :return: The end result is a .json and a .md file for every git repository.
    Can be found inside hg_files/
    """
    from fic_modules.markdown_modules import create_hg_md_table
    if onerepo:
        complete_data = {}
        repository_url = REPOSITORIES\
            .get("Mercurial")\
            .get(repositories_holder)\
            .get("url")
        folders_to_check = [folder for folder in REPOSITORIES
                            .get("Mercurial")
                            .get(repositories_holder)
                            .get("configuration")
                            .get("folders-to-check")]
        filter_hg_commit_data(repositories_holder,
                              folders_to_check,
                              repository_url)
        work_path = WORKING_DIR + "/hg_files/"
        repo_data = populate_changelog_json(work_path, repositories_holder)
        complete_data.update(repo_data)
        create_hg_md_table(repositories_holder)
    else:
        complete_data = {}
        for repo in repositories_holder["Mercurial"]:
            repository_name = repo
            repository_url = repositories_holder\
                .get("Mercurial")\
                .get(repo).get("url")
            folders_to_check = [folder for folder in repositories_holder
                                .get("Mercurial")
                                .get(repo).get("configuration")
                                .get("folders-to-check")]
            filter_hg_commit_data(repository_name,
                                  folders_to_check,
                                  repository_url)
            work_path = WORKING_DIR + "/hg_files/"
            repo_data = populate_changelog_json(work_path, repository_name)
            complete_data.update(repo_data)
            create_hg_md_table(repository_name)
    return complete_data


def filter_hg_commit_data(repository_name, folders_to_check, repository_url):
    """
    This function generates data for hg json files
    :param repository_url:
    :param folders_to_check:
    :param repository_name: name of the repository
    :return: Writes data in hg json files
    """
    LOGGER.info("Repo url: %s", repository_url)
    link = generate_hg_pushes_link(repository_name, repository_url)
    data = json.loads(requests.get(link).text)
    last_push_id = data.get("lastpushid")
    hg_repo_data = {}
    number = 0
    hg_repo_data.update({"0": {"last_push_id": last_push_id}})
    for key in data.get("pushes"):
        number += 1
        changeset_number = key
        changeset_pusher = data.get("pushes").get(key).get("user")
        date_of_push = data.get("pushes").get(key).get("date")
        hg_repo_data.update({number: {
            "changeset_number": changeset_number,
            "pusher": changeset_pusher,
            "date_of_push": time.strftime('%Y-%m-%d %H:%M:%S', time.
                                          localtime(date_of_push)),
            "changeset_commits": {}
        }})
        counter, counter2, counter3 = 0, 0, 0
        for keys in data.get("pushes").get(key).get("changesets"):
            counter = [x + 1 for x in range(len(data.get("pushes")
                                                .get(key)
                                                .get("changesets")))]
            node = keys.get("node")
            url = repository_url + "pushloghtml?changeset=" + node[:12]
            author = keys.get("author")
            desc = keys.get("desc")
            files_changed = []
            for entry in keys.get("files"):
                files_changed.append(entry)
            try:
                counter2 = counter[counter3]
                counter3 += 1
            except IndexError:
                pass
            if folders_to_check:
                if compare_files(files_changed, folders_to_check):
                    hg_repo_data[number]["changeset_commits"].update({
                        counter2: {
                            "url": url,
                            "commiter_name": author,
                            "commit_message": desc,
                            "files_changed": files_changed}})
        if hg_repo_data[number].get('changeset_commits') == {}:
            hg_repo_data.pop(number)
    json_writer_hg(repository_name, hg_repo_data)


def json_writer_hg(repository_name, new_commits):
    """
    :param repository_name:
    :param new_commits: a dictionary with the new commits
    :return: write the json file with the old and the new commits
    """
    hg_json_filename = "{}.json".format(repository_name)
    try:
        with open(WORKING_DIR + "/hg_files/" + hg_json_filename, "r") as\
                commit_json:
            # loads the content of existing json into a variable
            json_content = json.load(commit_json)
            number = len(json_content) - 1
            if json_content['0']:
                json_content['0'].update(new_commits['0'])
            if len(new_commits) > 1:
                for commit in new_commits:
                    if commit != '0':
                        json_content.update({int(number): new_commits[commit]})
                        number += 1
            json_file = open(WORKING_DIR + "/hg_files/" + hg_json_filename,
                             "w")
            json.dump(json_content, json_file, indent=2)
            json_file.close()
    except FileNotFoundError:
        json_content = {}
        number = 0
        for commit in new_commits:
            json_content.update({int(number): new_commits[commit]})
            number += 1
        json_file = open(WORKING_DIR + "/hg_files/" + hg_json_filename, "w")
        json.dump(json_content, json_file, indent=2)
        json_file.close()


def extract_json_from_hg(repo_name, days_to_generate):
    """
    Extracts the json data from json files and writes the data to the main
    markdown table file.
    The function looks into json files after the last commit, extracts it and
    calls the write_main_md_table function.
    :param days_to_generate:
    :param repo_name:
    :return: none
    """
    from fic_modules.markdown_modules import generate_markdown_header,\
        write_main_md_table
    from fic_modules.helper_functions import generate_repository_url

    nr_days_ago = datetime.utcnow() - timedelta(days=days_to_generate)
    # nr_days_ago = datetime.strftime(nr_days_ago, "%Y-%m-%d %H:%M:%S")

    with open("./changelog.json") as json_file:
        data = json.load(json_file)

        for repo_name in repo_name:
            repository_url = generate_repository_url("hg_files", repo_name, "md")
            repository_json = generate_repository_url("hg_files", repo_name, "json")

            try:
                generate_markdown_header("changelog.md",
                                         repo_name,
                                         repository_url,
                                         repository_json)
                count_pushes = 0
                for changeset_iterator in data.get("Hg").get(repo_name):
                    for commit_iterator in data.get("Hg").get(repo_name) \
                            .get(changeset_iterator)\
                            .get("changeset_commits"):
                        commit_date = data.get("Hg").get(repo_name) \
                            .get(changeset_iterator)\
                            .get("date_of_push")
                        commit_date = datetime.strptime(commit_date,
                                                        "%Y-%m-%d %H:%M:%S")

                        if commit_date > nr_days_ago:
                            count_pushes = count_pushes + 1
                            commit_description = data.get("Hg")\
                                .get(repo_name)\
                                .get(changeset_iterator) \
                                .get("changeset_commits") \
                                .get(commit_iterator) \
                                .get("commit_message")
                            commit_description = \
                                remove_chars(commit_description, "\n")
                            commit_description = \
                                replace_bug_with_url(commit_description, LOGGER)
                            commit_url = data.get("Hg").get(repo_name)\
                                .get(changeset_iterator) \
                                .get("changeset_commits") \
                                .get(commit_iterator) \
                                .get("url")
                            commit_url = "[Link](" + commit_url + ")"
                            author = data.get("Hg")\
                                .get(repo_name)\
                                .get(changeset_iterator)\
                                .get("pusher")
                            review = extract_reviewer(commit_description)
                            write_main_md_table("changelog.md",
                                                commit_url,
                                                commit_description,
                                                author,
                                                review,
                                                commit_date)
                if count_pushes == 0:
                    commit_url = " "
                    if days_to_generate == 1:
                        commit_description = "No push in the last day.. " \
                                             "[see the history of MD " \
                                             "commits](" + \
                                             repository_url + \
                                             ")"
                    else:
                        commit_description = "No push in the last " + \
                                             str(days_to_generate) + \
                                             " days.. [see the history of MD" \
                                             " commits](" + \
                                             repository_url + \
                                             ")"
                    author = "FIC - BOT"
                    review = "Self Generated"
                    commit_date = " - "
                    write_main_md_table("changelog.md",
                                        commit_url,
                                        commit_description,
                                        author,
                                        review,
                                        commit_date)
            except AttributeError:
                LOGGER.exception("Attribute Error!! \n Probable issue is a "
                                 "malfunctioned json file.. Please check the "
                                 "following file: %s", repo_name)
            except KeyError:
                LOGGER.exception("File %s is empty. Please check: %s for more "
                                 "details.", repo_name, repository_url)

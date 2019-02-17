import json
import requests
import time
from urllib.request import urlopen
from datetime import (
    datetime,
    timedelta
)
from fic_modules.configuration import (
    REPOSITORIES,
    LOGGER,
    WORKING_DIR,
    NUMBER_OF_CHANGESETS
)
from fic_modules.helper_functions import (
    remove_chars,
    compare_files,
    extract_reviewer
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
    except FileNotFoundError:
        last_stored_push_id = 0
    if LOGGER:
        print("Last local push id is : ", last_stored_push_id)
    return last_stored_push_id


def generate_hg_pushes_link(repo_name, repository_url):
    """
    :param repo_name: name of the repo we are currently working on
    :param repository_url: base repository url stored in repositories.json
    :return: generate_pushes_link: a link used for bringing data from HG
    """
    start_id = get_last_local_push_id(repo_name)
    url = repository_url + "json-pushes?version=2"
    response = urlopen(url)
    data = json.loads(response.read())
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
        create_hg_md_table(repositories_holder)
    else:
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
            create_hg_md_table(repository_name)


def filter_hg_commit_data(repository_name, folders_to_check, repository_url):
    """
    This function generates data for hg json files
    :param repository_url:
    :param folders_to_check:
    :param repository_name: name of the repository
    :return: Writes data in hg json files
    """
    if LOGGER:
        print("Repo url:", repository_url)
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
                    if commit != new_commits[0]:
                        json_content.update({int(number): commit})
                        number += 1
            json_file = open(WORKING_DIR + "/hg_files/" + hg_json_filename, "w")
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



def extract_json_from_hg(json_files, path_to_files, days_to_generate):
    """
    Extracts the json data from json files and writes the data to the main
    markdown table file.
    The function looks into json files after the last commit, extracts it and
    calls the write_main_md_table function.
    :param days_to_generate:
    :param json_files: List of files to extract commits from.
    :param path_to_files: Folder to json files
    :return: none
    """
    from fic_modules.markdown_modules import generate_markdown_header, write_main_md_table
    time_24h_ago = datetime.utcnow() - timedelta(days=days_to_generate)
    test = datetime.strftime(time_24h_ago, "%Y-%m-%d %H:%M:%S")
    time_24h_ago = datetime.strptime(test, "%Y-%m-%d %H:%M:%S")

    for file in json_files:
        count_pushes = 0
        file_path = "{}/".format(path_to_files) + file
        with open(file_path) as json_file:
            data = json.load(json_file)
            base_link = "https://github.com/mozilla-releng/firefox-infra-" \
                        "changelog/blob/master/{}/"\
                        .format(path_to_files)
            repository_url = base_link + file \
                .rstrip() \
                .replace(" ", "%20") \
                .rstrip() \
                .replace(".json", ".md")
            repository_json = base_link + file \
                .rstrip() \
                .replace(" ", "%20")
            repository_title = file.replace(".json", "")

            try:
                generate_markdown_header("changelog.md",
                                         repository_title,
                                         repository_url,
                                         repository_json)
                if "0" in data:
                    del data["0"]
                for changeset_iterator in data:
                    for commit_iterator in data\
                            .get(changeset_iterator)\
                            .get("changeset_commits"):
                        commit_date = data\
                            .get(changeset_iterator)\
                            .get("date_of_push")
                        is_it_under_24 = datetime.strptime(commit_date,
                                                           "%Y-%m-%d %H:%M:%S")
                        if is_it_under_24 > time_24h_ago:
                            count_pushes = count_pushes + 1
                            commit_description = data.get(changeset_iterator) \
                                .get("changeset_commits") \
                                .get(commit_iterator) \
                                .get("commit_message")
                            commit_description = \
                                remove_chars(commit_description, "\n")
                            commit_url = data.get(changeset_iterator) \
                                .get("changeset_commits") \
                                .get(commit_iterator) \
                                .get("url")
                            commit_url = "[Link](" + commit_url + ")"
                            author = data.get(changeset_iterator).get("pusher")
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
                if LOGGER:
                    print("Attribute Error!! \n "
                          "Probable issue is an malfunctioned json file.. "
                          "Please check the following file:", file)
            except KeyError:
                if LOGGER:
                    print("File ", file, " is empty. \n",
                          "Please check:",
                          repository_url,
                          " for more details.\n")

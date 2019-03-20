"""
This module handles the git generation, filtering and other git related stuff.
"""

import json
import re
from datetime import (
    datetime,
    timedelta
)
import requests
from dateutil.parser import parse
from fic_modules.configuration import (
    LAST_MONTH,
    GIT,
    REPOSITORIES,
    WORKING_DIR,
    LOGGER
)
from fic_modules.helper_functions import (
    remove_chars,
    limit_checker,
    get_commit_details,
    compare_files,
    populate_changelog_json
)
from fic_modules.markdown_modules import (
    create_git_md_table,
    create_md_table_for_scriptworkers
)


def filter_git_commit_data(repository_name, repository_team, repository_type,
                           folders_to_check):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function
    from 're' library
    :param repository_team:
    :param repository_name: name of the given repo
    :param repository_type: type of a repo we are going to work with
    :param folders_to_check: list that contains every folder we care about
    from given repo
    :return: Filtered json data
    TODO: please add the exception blocks since the script fails when it can't
    pull data:
    (e.g raise self.__createException(status, responseHeaders, output)
    github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """

    repository_path = repository_team + repository_name
    # TYPE = NO-TAG
    if repository_type == "no-tag":
        filter_git_no_tag(repository_name, repository_path, folders_to_check)
    # TYPE = COMMIT-KEYWORD
    if repository_type == "commit-keyword":
        filter_git_commit_keyword(repository_name, repository_path)
    # TYPE = TAG
    if repository_type == "script":
        filter_git_scriptworkers(repository_team, repository_name)
    if repository_type == "tag":
        if repository_name == "build-puppet":
            filter_git_tag_bp(repository_name,
                              repository_path)
        elif repository_name != "build-puppet":
            filter_git_tag(repository_name, repository_team, repository_path)


def create_files_for_git(repositories_holder, onerepo):
    """
    Main GIT function. Takes every Git repo from a .json file which is
    populated with repositories and writes all the commit data of each repo in
    a json and MD file formats.
    :param: repositories_holder: Expects a .json file that contains a list of
    repositories.
    :return: The end result is a .json and a .md file for every git repository.
    Can be found inside git_files/
    """
    if onerepo:
        complete_data = {}
        repository_team = REPOSITORIES \
            .get("Github") \
            .get(repositories_holder) \
            .get("team")
        repository_type = REPOSITORIES \
            .get("Github") \
            .get(repositories_holder) \
            .get("configuration") \
            .get("type")
        LOGGER.info("Working on repo: {}".format(repositories_holder))
        folders_to_check = [folder for folder in REPOSITORIES
            .get("Github")
            .get(repositories_holder)
            .get("configuration")
            .get("folders-to-check")]
        filter_git_commit_data(repositories_holder,
                               repository_team,
                               repository_type,
                               folders_to_check)
        if repositories_holder == "build-puppet":
            create_git_md_table(repositories_holder, "git_files")
            create_md_table_for_scriptworkers(repositories_holder)
        else:
            create_git_md_table(repositories_holder, "git_files")
        work_path = WORKING_DIR + "/git_files/"
        repo_data = populate_changelog_json(work_path, repositories_holder)
        complete_data.update(repo_data)
        LOGGER.info("MD table generated successfully for {}"
                    .format(repositories_holder))
    else:
        complete_data = {}
        for repo in repositories_holder["Github"]:
            repository_name = repo
            repository_team = repositories_holder \
                .get("Github") \
                .get(repo) \
                .get("team")
            repository_type = repositories_holder \
                .get("Github") \
                .get(repo) \
                .get("configuration") \
                .get("type")
            LOGGER.info("Working on repo: {}".format(repository_name))
            folders_to_check = [folder for folder in repositories_holder
                .get("Github")
                .get(repo)
                .get("configuration")
                .get("folders-to-check")]
            filter_git_commit_data(repository_name,
                                   repository_team,
                                   repository_type,
                                   folders_to_check)
            if repository_name == "build-puppet":
                create_git_md_table(repository_name, "git_files")
                create_md_table_for_scriptworkers(repository_name)
            else:
                create_git_md_table(repository_name, "git_files")
            work_path = WORKING_DIR + "/git_files/"
            repo_data = populate_changelog_json(work_path, repository_name)
            complete_data.update(repo_data)
            LOGGER.info("MD table generated successfully")
            LOGGER.info("Finished working on {}".format(repository_name))
    return complete_data


def filter_git_tag_bp(repository_name, repository_path):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function
    from 're' library
    :param repository_name: name of the given repo
    :param repository_path:
    :return: the commits into a dictionary
    TODO: please add the exception blocks since the script fails when it can't
    pull data:
    (e.g raise self.__createException(status, responseHeaders, output)
    github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    number = 0
    commit_number_tracker = 1
    pathway = REPOSITORIES.get("Github") \
        .get(repository_name) \
        .get("configuration") \
        .get("files-to-check")
    last_checked = last_check(repository_name)
    new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow())}}

    if limit_checker():
        new_commits = GIT.get_repo(repository_path) \
            .get_commits(since=last_checked)

    for commit in new_commits:
        each_commit = {}
        switch = False
        LOGGER.info("Commit number: " + str(commit_number_tracker))
        commit_number_tracker += 1
        files_changed_by_commit = [x.filename for x in commit.files]
        LOGGER.info(files_changed_by_commit)
        LOGGER.info(len(files_changed_by_commit))
        changed_file_number = 1
        for entry in files_changed_by_commit:
            LOGGER.info("changed file number: {} "
                        .format(changed_file_number))
            LOGGER.info(entry)
            changed_file_number += 1
            for scriptworkers in pathway:
                LOGGER.info("checking repo:{} ".format(scriptworkers))
                if entry in pathway[scriptworkers]:
                    LOGGER.debug("This commit needs to be saved")
                    switch = True
                    break
        if switch:
            number += 1
            each_commit.update({int(number): get_commit_details(commit)})
            new_commit_dict.update(each_commit)
    json_writer_git(repository_name, new_commit_dict)


def filter_git_scriptworkers(repo_team, script_repo):
    """
    Filters the scriptworker repos that are under build-puppet
    :param repo_team: team name as a string
    :param script_repo: scriptworker repo we are working on
    :return: returns the new commits of a repo
    """
    last_local_date = get_date_from_json(script_repo)
    latest_releases = get_version(script_repo, repo_team)
    with open("./repositories.json", "r") as file:
        json_content = json.load(file)
        version_path = json_content.get("Github").get(script_repo) \
            .get("configuration").get("version-path")
    checker = compare_versions(version_path, script_repo, latest_releases)
    if checker:
        new_commit_version_date = \
            datetime.strptime(latest_releases
                              .get("latest_release")
                              .get("date"),
                              "%Y-%m-%d %H:%M:%S")
        commit_number = 0
        new_scriptworker_dict = {
            (int(commit_number)): {"lastChecked": str(datetime.utcnow()),
                                   "last_releases": latest_releases}}
        new_repo_path = repo_team + script_repo
        for commit2 in GIT.get_repo(new_repo_path).get_commits(
                since=last_local_date):
            last_modified = \
                datetime.strftime(parse(commit2.last_modified),
                                  "%Y-%m-%d %H:%M:%S")
            last_modified = datetime.strptime(last_modified,
                                              "%Y-%m-%d %H:%M:%S")
            if last_modified <= new_commit_version_date:
                each_commit2 = {}
                commit_number += 1
                commit_details = get_commit_details(commit2)
                # if commit contain tag
                    each_commit2.update({int(commit_number): commit_details})
                    new_scriptworker_dict.update(each_commit2)
                # else:
                #   pass
        json_writer_git(script_repo, new_scriptworker_dict)
    else:
        LOGGER.info("No new changes entered production")


def filter_git_tag(repository_name, repository_team, repository_path):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function
    from 're' library
    :param repository_team: the team of the given repo
    :param repository_name: name of the given repo
    :param repository_path:
    :return: the commits into a dictionary
    TODO: please add the exception blocks since the script fails when it can't
    pull data:
    (e.g raise self.__createException(status, responseHeaders, output)
     github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    number = 0
    latest_releases = get_version(repository_name, repository_team)
    with open("repositories.json", "r") as file:
        json_content = json.load(file)
        version_path = json_content.get("Github").get(repository_name) \
            .get("configuration").get("version-path")
    checker = compare_versions(version_path, repository_name, latest_releases)
    if checker:
        last_commit_date = get_date_from_json(repository_name)
        new_version_commit_date = datetime.strptime(latest_releases
                                                    .get("latest_release")
                                                    .get("date"),
                                                    "%Y-%m-%d %H:%M:%S")
        new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow()),
                                 "last_releases": latest_releases}}
        for commit in GIT.get_repo(repository_path) \
                .get_commits(since=last_commit_date):
            last_modified = datetime.strftime(parse(commit.last_modified),
                                              "%Y-%m-%d %H:%M:%S")
            last_modified = datetime.strptime(last_modified,
                                              "%Y-%m-%d %H:%M:%S")
            if last_modified <= new_version_commit_date:
                each_commit = {}
                number += 1
                each_commit.update({int(number): get_commit_details(commit)})
                new_commit_dict.update(each_commit)
        json_writer_git(repository_name, new_commit_dict)
    else:
        LOGGER.info("No new changes entered production")


def get_version(repo_name, repo_team):
    """
    Gets the latest 2 versions released for a repository on github.
    :param repo_name: repository name
    :param repo_team: repository team
    :return: a dictionary with information from the last two release versions:
     latestRelease and previousRelease
    """
    repo_path = repo_team + repo_name
    iteration = 0
    empty_dict = {}
    for tags in GIT.get_repo(repo_path).get_tags():
        version = tags.name
        sha = tags.commit.sha
        date = tags.commit.commit.last_modified
        date_format = parse(date)
        date = date_format.strftime("%Y-%m-%d %H:%M:%S")
        author = tags.commit.author.login
        if iteration == 0:
            latest_release = {"version": version,
                              "sha": sha,
                              "date": date,
                              "author": author
                              }
            empty_dict.update({"latest_release": latest_release})
            break
    return empty_dict


def get_version_from_build_puppet(version_path, repo_name):
    """
    Gets the latest version released for a scriptworker repository on github.
    :param: version_path: Path to the requirements.txt where the version number
     is stored
    :param: repo_name: The repo for which we are checking the version.
    :return: Returns the version number that is stored in build-puppet for
    each scriptworker
    """
    file_to_string = requests.get(version_path).text.split()
    for word in file_to_string:
        if repo_name in word:
            version_in_puppet = re.split("\\b==\\b", word)[-1]
            if version_in_puppet != repo_name:
                return version_in_puppet


def json_writer_git(repository_name, new_commits):
    """
    :param repository_name: repository name
    :param new_commits: a dictionary with the new commits
    :return: write the json file with the old and the new commits
    """
    git_json_filename = "{}.json".format(repository_name)
    try:
        with open(WORKING_DIR + "/git_files/" + git_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
    except FileNotFoundError:
        json_content = ""
    if len(json_content) > 1:
        number = len(new_commits) - 1
        for old_commit in json_content:
            if old_commit != "0":
                number += 1
                new_commits.update({int(number): json_content[old_commit]})

    if new_commits:
        json_file = open(WORKING_DIR + "/git_files/" + git_json_filename, "w")
        json.dump(new_commits, json_file, indent=2)
        json_file.close()


def last_check(repository_name):
    """
    :param repository_name: Repository name to be checked.
    :return: the last time when the repository was checked
    """
    git_json_filename = "{}.json".format(repository_name)
    try:
        with open(WORKING_DIR + "/git_files/" + git_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
            try:
                last_checked = datetime.strptime(json_content
                                                 .get("0")
                                                 .get("lastChecked"),
                                                 "%Y-%m-%d %H:%M:%S")
                LOGGER.info("Repo last updated on: " + str(last_checked))

            except ValueError:
                last_checked = datetime.strptime(json_content
                                                 .get("0")
                                                 .get("lastChecked"),
                                                 "%Y-%m-%d %H:%M:%S.%f")
                LOGGER.info("Repo last updated on: " + str(last_checked))

    except IOError:
        last_checked = LAST_MONTH
    return last_checked


def get_version_from_json(repo_name):
    """
    :param repo_name: name of the repo we are working on
    :return: version our repo was bumped to by the last local commit that we
    have
    """
    git_json_filename = "{}.json".format(repo_name)
    try:
        with open(WORKING_DIR + "/git_files/" + git_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
        last_stored_version = json_content \
            .get("0") \
            .get("last_releases") \
            .get("latest_release") \
            .get("version")
    except FileNotFoundError:
        last_stored_version = ""
    return last_stored_version


def get_date_from_json(repo_name):
    """
    :param repo_name: name of the repo we are currently working on
    :return: date of the last commit that we have locally in our json
    """
    git_json_filename = "{}.json".format(repo_name)
    try:
        with open(WORKING_DIR + "/git_files/" + git_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
        last_stored_date = json_content \
            .get("0") \
            .get("last_releases") \
            .get("latest_release") \
            .get("date")
        date_format = parse(last_stored_date)
        last_stored_date = datetime.strptime(str(date_format),
                                             "%Y-%m-%d %H:%M:%S")
    except FileNotFoundError:
        last_stored_date = datetime.strptime("2019-01-01 01:00:00",
                                             "%Y-%m-%d %H:%M:%S")
        LOGGER.info("last local date was: {} ".format(last_stored_date))
    return last_stored_date


def filter_git_no_tag(repository_name, repository_path, folders_to_check):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function
     from 're' library
    :param repository_name: name of the given repo
    :param repository_path:
    :param folders_to_check: the folders we care about
    :return: the commits into a dictionary
    TODO: please add the exception blocks since the script fails when it
    can't pull data:
    (e.g raise self.__createException(status, responseHeaders, output)
    github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    number = 0
    last_checked = last_check(repository_name)
    new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow())}}
    if limit_checker():
        new_commits = GIT.get_repo(repository_path) \
            .get_commits(since=last_checked)

    for commit in new_commits:
        each_commit = {}
        if folders_to_check:
            files_changed = []
            for entry in commit.files:
                files_changed.append(entry.filename)
            if compare_files(files_changed, folders_to_check):
                number += 1
                each_commit.update({int(number): get_commit_details(commit)})
                new_commit_dict.update(each_commit)
        else:
            number += 1
            each_commit.update({int(number): get_commit_details(commit)})
            new_commit_dict.update(each_commit)
    json_writer_git(repository_name, new_commit_dict)
    return True


def filter_git_commit_keyword(repository_name, repository_path):
    """
    Filters out only the data that we need from a commit
    Substitute the special characters from commit message using 'sub' function
    from 're' library
    :param repository_name: name of the given repo
    :param repository_path:
    :return: the commits into a dictionary
    TODO: please add the exception blocks since the script fails when it can't
    pull data:
    (e.g raise self.__createException(status, responseHeaders, output)
    github.GithubException.GithubException: 502 {'message': 'Server Error'}
    """
    number = 0
    last_checked = last_check(repository_name)
    new_commit_dict = {"0": {"lastChecked": str(datetime.utcnow())}}
    if limit_checker():
        new_commits = GIT.get_repo(repository_path) \
            .get_commits(since=last_checked)

    for commit in new_commits:
        files_changed_by_commit = [x.filename for x in commit.files]
        if files_changed_by_commit:
            each_commit = {}
            LOGGER.info(commit.commit.message)
            if "deploy" in commit.commit.message:
                number += 1
                each_commit.update({int(number): get_commit_details(commit)})
                new_commit_dict.update(each_commit)
    json_writer_git(repository_name, new_commit_dict)


def compare_versions(version_path, scriptworker_repo, latest_releases):
    """
    Checks the version of a scriptworker repo from its changelog, build-puppet
    and locally saved one against each other
    :param version_path:
    :param scriptworker_repo:
    :param latest_releases:
    :return:
    """

    version_in_puppet = get_version_from_build_puppet(version_path,
                                                      scriptworker_repo)
    last_local_version = get_version_from_json(scriptworker_repo)
    check_release = latest_releases.get("latest_release").get("version")

    if version_in_puppet == check_release:
        expr1 = bool(version_in_puppet != last_local_version)
        expr2 = bool(last_local_version != check_release)

        return True if (expr1 or expr2) else False
    else:
        return True


def extract_json_from_git(repository, days_to_generate):
    """
    Extracts the json data from json files and writes the data to the main
    markdown table file.
    The function looks into json files after the last commit, extracts it and
    calls the write_main_md_table function.
    :param days_to_generate:
    :param repository:
    :return: none
    """
    from fic_modules.markdown_modules import generate_markdown_header, \
        write_main_md_table
    from fic_modules.helper_functions import generate_repository_url

    nr_days_ago = datetime.utcnow() - timedelta(days=days_to_generate)

    count_pushes = 0
    with open("./changelog.json") as json_file:
        data = json.load(json_file)

        repo = str(repository)
        repository_url = generate_repository_url("git_files", repo, "json")
        repository_json = generate_repository_url("git_files", repo, "md")

        try:
            generate_markdown_header("changelog.md",
                                     repo,
                                     repository_url,
                                     repository_json)
            if "0" in data:
                del data["0"]

            for commit_iterator in data.get("Github").get(repo):
                commit_number = str(commit_iterator)

                commit_date = data.get("Github")\
                    .get(repo)\
                    .get(commit_number)\
                    .get("commit_date")
                commit_date = datetime.strptime(commit_date, "%Y-%m-%d %H:%M:%S")

                if commit_date > nr_days_ago:
                    count_pushes = count_pushes + 1
                    commit_description = data.get("Github").get(repo) \
                        .get(commit_number) \
                        .get("commit_message")
                    commit_description = remove_chars(commit_description,
                                                      "\U0001f60b")
                    commit_url = data.get("Github")\
                        .get(repo)\
                        .get(commit_number)\
                        .get("url")
                    commit_url = "[Link](" + commit_url + ")"

                    author = data.get("Github")\
                        .get(repo)\
                        .get(commit_number)\
                        .get("commiter_name")
                    review = "N/A"
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
                                         repository_json + \
                                         ")"
                else:
                    commit_description = "No push in the last " + \
                                         str(days_to_generate) + \
                                         " days.. [see the history of MD" \
                                         " commits](" + \
                                         repository_json + \
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
        except KeyError:
            LOGGER.info("File " + repo + " is empty. \nPlease check:" +
                        str(repository_url) + " for more details.\n")

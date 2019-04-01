"""
This module contains all of the markdown generation and writing to the files.
"""
import json
import re
from datetime import datetime
from fic_modules.helper_functions import (
    filter_strings,
    remove_chars,
    replace_bug_with_url,
    trim_commit_description
)
from fic_modules.configuration import (
    LAST_WEEK,
    REPOSITORIES,
    LOGGER,
    WORKING_DIR
)
from fic_modules.hg import extract_json_from_hg


def create_git_md_table(repository_name, path_to_files):
    """
    Uses 'repository_name' parameter to generate markdown tables for every
    json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of
    the MD table
    :param path_to_files: Used to store path to json files (git_files,
    hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(
            "/{}/"
            .format(path_to_files) + "{}.json"
            .format(repository_name))\
            .read()
        data = json.loads(json_data)
        base_table = "| Commit Number | Commiter | Commit " \
                     "Message | Commit Url | Date | \n" + \
                     "|:---:|:----:|:---------------------" \
                     "-------------:|:------:|:----:| \n"
        tables = {}
        try:
            version = data\
                .get('0')\
                .get("last_two_releases")\
                .get("LatestRelease")\
                .get("version")
            date = data\
                .get('0')\
                .get("last_two_releases")\
                .get("LatestRelease")\
                .get("date")
            md_title = [
                "Repository name: {}\n Current version: {} released on {}"
                .format(repository_name, version, date)]
        except AttributeError:
            md_title = ["{} commit markdown table since {}"
                        .format(repository_name, LAST_WEEK)]

        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            try:
                commit_author = data.get(key).get("commiter_name")
                commit_author = re.sub("\u0131", "i", commit_author)
                date = data.get(key).get("commit_date")
                url = data.get(key).get("url")
                message = data.get(key).get("commit_message")
                message = trim_commit_description(message, url)
                message = remove_chars(message, "\U0001f60b")
                message = re.sub("\|", "\|", message)

                commit_author = filter_strings(commit_author)
                message = filter_strings(message)
                message = replace_bug_with_url(message, LOGGER)
                row = "|" + commit_number + \
                      "|" + commit_author + \
                      "|" + message + \
                      "|" + "[URL](" + url + ")" + \
                      "|" + date + "\n"

                del commit_number_list[-1]
                for repo in tables.keys():
                    tables[repo] = tables[repo] + row
            except TypeError:
                pass

        md_file_name = "{}.md".format(repository_name)
        md_file = open("/{}/".format(path_to_files) +
                       md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        LOGGER.info("Json for %s is empty! Skipping!", repository_name)


def create_md_table_for_scriptworkers(repository_name):
    """
    This function creates the markdown table for the scriptworker repositories.
    :param: repositories_name: Expects the name of the repository
    :return: a call to 'create_md_table' function for each scriptworker
    repositories
    """
    files_to_check = [x for x in REPOSITORIES
                      .get("Github")
                      .get(repository_name)
                      .get("configuration")
                      .get("files-to-check")]
    for scriptworker_repo in files_to_check:
        create_git_md_table(scriptworker_repo, "git_files")


def generate_main_md_table(repositories_holder, which_repo, days_to_generate):
    """
    Looks into repositories folders (hg_files & git files),
    filters the files to load the json's using a passfilter and calls after
    extraction functions.
    :param which_repo: tells the function for which repo to update the md
    :param days_to_generate: just a pass by parameter, used in extract json
    from git/hg and generates for the specified days.
    :param repositories_holder: repositories
    """
    from fic_modules.git import extract_json_from_git
    successfully_generated = "part from main markdown table was " \
                             "successfully generated."
    list = []
    for i in repositories_holder.get("Github"):
        position = repositories_holder.get("Github").get(i).get("order")
        list.append((position, i, "git"))
    for i in repositories_holder.get("Mercurial"):
        position = repositories_holder.get("Mercurial").get(i).get("order")
        list.append((position, i, "hg"))
    list.sort()
    for element in list:
        if (which_repo == "complete" or which_repo == "Git") and element[2] == "git":
            extract_json_from_git(element[1], days_to_generate)
            LOGGER.info("GIT %s Repository: %s", successfully_generated, element[1])

        if (which_repo == "complete" or which_repo == "Hg") and element[2] == "hg":
            extract_json_from_hg(element[1], days_to_generate)
            LOGGER.info("HG %s Repository: %s", successfully_generated, element[1])

        if which_repo != "complete" and which_repo != "Git" and which_repo != "Hg":
            LOGGER.error("No {} table was generated!".format(element[2]))


def write_date_header(file_name, datetime_object):
    """
    This function writes a date from a specific datetime object into a file as
     a date header.
    :param file_name: name of the file to be written to.
    :param datetime_object: datetime object used for write to file.
    :return:
    """
    file = open(file_name, "a")

    base_table = "|            | \n" + \
                 "|:----------:| \n"
    date_header = "| Generated on: " + \
                  str(datetime.utcnow()) + \
                  " and contains modifications from: " + \
                  str(datetime_object) + \
                  " |"
    file.write("\n" + base_table + date_header + "\n")
    file.close()
    LOGGER.info("Generated date header for file: %s with datestamp %s",
                    str(file_name), str(datetime.utcnow()))


def create_hg_md_table(repository_name):
    """
    Uses 'repository_name' parameter to generate markdown tables for every
    json file inside path_to_files parameter.
    :param repository_name: Used to display the repo name in the title row of
    the MD table
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open("hg_files/" + "{}.json"
                         .format(repository_name)).read()
        data = json.loads(json_data)
        base_table = "| Changeset | Date | Commiter | " \
                     "Commit Message | Commit URL | \n" + \
                     "|:---:|:---:|:----:|:---------------" \
                     "-------------------:|:-----:| \n"
        tables = {}
        try:
            last_push_id = data.get('0').get("last_push_id")
            md_title = [
                "Repository name: {}\n Current push id: {}"
                .format(repository_name, last_push_id)]
        except AttributeError:
            md_title = ["Error while accessing the " +
                        str(repository_name) + "file."]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            if key > "0":
                key = str(len(data) - int(key))
                changeset_id = data.get(key).get("changeset_number")
                date_of_push = data.get(key).get("date_of_push")
                try:
                    for entry in data.get(key).get("changeset_commits"):
                        try:
                            commit_author = data \
                                .get(key) \
                                .get("changeset_commits") \
                                .get(entry) \
                                .get("commiter_name")
                            commit_author = re.sub("\u0131", "i",
                                                   commit_author)
                            commit_author = filter_strings(commit_author)

                            url = data \
                                .get(key) \
                                .get("changeset_commits") \
                                .get(entry) \
                                .get("url")

                            message = data \
                                .get(key) \
                                .get("changeset_commits") \
                                .get(entry).get("commit_message")
                            message = re.sub("\n|", "", message)
                            message = filter_strings(message)
                            message = trim_commit_description(message, url)
                            message = replace_bug_with_url(message, LOGGER)

                            row = "|" + changeset_id + \
                                  "|" + date_of_push + \
                                  "|" + commit_author + \
                                  "|" + message + \
                                  "|" + url + "\n"

                            for repo in tables.keys():
                                tables[repo] = tables[repo] + row
                        except TypeError:
                            pass
                except TypeError:
                    pass

        md_file_name = "{}.md".format(repository_name)
        md_file = open("hg_files/" + md_file_name, "w")

        try:
            for key, value in tables.items():
                if value != base_table:
                    md_file.write("## " + key.upper() + "\n\n")
                    md_file.write(value + "\n\n")
        except KeyError:
            pass

        md_file.close()
    except FileNotFoundError:
        LOGGER.error("Json for %s is empty! Skipping!", repository_name)


def generate_markdown_header(file_name, repository_name, markdown_link,
                             json_link):
    """
    This function appends the markdown header to the main markdown table.
    It includes the repository title (name), the markdown link and the json
    link.
    :param file_name: name of the file in which the content it's added.
    :param repository_name: name of the repository for the generated table.
    :param markdown_link: markdown link for the header table.
    :param json_link: json link for the header table.
    :return: none, expected to write to file_name.
    """
    file = open(file_name, "a")

    repository_title = "|\t" + repository_name + "\t|\t" + \
                       "[MarkDown](" + markdown_link + ")" + \
                       "\t|\t" + "[Json](" + \
                       json_link + ")" + "\t| \n"

    title_table_formation = "|:----------:|:-----------" \
                            "------------:|:--------:| \n "

    base_table = "| Link | Last commit | Author | " \
                 "Reviewer | Deploy time | \n" + \
                 "|:----------:|:-----------:|:---" \
                 "---:|:--------:|:-----------:| \n"

    file.write("\n" +
               repository_title +
               title_table_formation +
               "\n" + base_table)
    file.close()


def write_main_md_table(file_name, repository_url, last_commit, author,
                        reviewer, deploy_time):
    """
    This function opens a file (that file should be already created and
    appends to it a row that will contain the repository, the last commit and
    the deploy time.
    :param reviewer: Reviewer name
    :param author: Author name for the push/commit
    :param file_name: Name of the file in which the content is appended.
    (should also contain the path)
    :param repository_url: Repository url for the first element of the table.
    :param last_commit: Description of the last commit used as the 2nd element
     of the table
    :param deploy_time: Time and Time designator used as the 3rd element of
    the table
    :return:
    """
    last_commit = filter_strings(last_commit)
    author = filter_strings(author)
    reviewer = filter_strings(reviewer)

    row = "|" + repository_url + \
          "|" + last_commit + \
          "|" + author + \
          "|" + reviewer + \
          "|" + str(deploy_time) + \
          "|" + "\n"
    write_file = open(file_name, "a")
    write_file.write(row)
    write_file.close()


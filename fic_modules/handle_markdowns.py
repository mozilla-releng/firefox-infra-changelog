import json
import re
from fic_modules.helper_functions import remove_chars
from client import extract_json_from_hg, extract_json_from_git
import os
from os import listdir
from os.path import isfile, join
from datetime import datetime


def create_md_table(repository_name,
                    path_to_files,
                    current_dir,
                    last_week,
                    logger):
    """
    Uses 'repository_name' parameter to generate markdown tables for every
    json file inside path_to_files parameter.
    :param logger:
    :param last_week:
    :param current_dir:
    :param repository_name: Used to display the repo name in the title row of
    the MD table
    :param path_to_files: Used to store path to json files (git_files,
    hg_files)
    :return: MD tables for every json file inside the git_files dir.
    """

    try:
        json_data = open(
            current_dir + "/{}/"
            .format(path_to_files) + "{}.json"
            .format(repository_name))\
            .read()
        # print("JSON: ", json_data)
        data = json.loads(json_data)
        # print("JSON Data: ", data)
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
                        .format(repository_name, last_week)]

        commit_number_list = [key for key in data]

        for repo in md_title:
            tables[repo] = base_table

        for key in data:
            commit_number = commit_number_list[-1]
            try:
                commit_author = data.get(key).get("commiter_name")
                commit_author = re.sub("\u0131", "i", commit_author)
                date = data.get(key).get("commit_date")
                message = data.get(key).get("commit_message")
                message = remove_chars(message, "\U0001f60b")
                message = re.sub("\|", "\|", message)
                url = data.get(key).get("url")

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
        md_file = open(current_dir + "/{}/".format(path_to_files) +
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
        if logger:
            print("Json for {} is empty! Skipping!".format(repository_name))


def create_md_for_scriptworkers(repository_name,
                                repositories,
                                current_dir,
                                last_week,
                                logger):
    """
    This function creates the markdown table for the scriptworker repositories.
    :param: repositories_name: Expects the name of the repository
    :return: a call to 'create_md_table' function for each scriptworker
    repositories
    """
    files_to_check = [x for x in repositories
                      .get("Github")
                      .get(repository_name)
                      .get("configuration")
                      .get("files-to-check")]

    for scriptworker_repo in files_to_check:
        create_md_table(scriptworker_repo,
                        "git_files",
                        current_dir,
                        last_week,
                        logger)


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
    row = "|" + repository_url + \
          "|" + last_commit + \
          "|" + author + \
          "|" + reviewer + \
          "|" + deploy_time + \
          "|" + "\n"
    write_file = open(file_name, "a")
    write_file.write(row)


def write_date_header(file_name, datetime_object, logger):
    """
    This function writes a date from a specific datetime object into a file as
     a date header.
    :param logger:
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
    if logger:
        print("Generated date header for file:", file_name, " with datestamp",
              str(datetime.utcnow()))


def generate_main_md_table(path_to_files, logger, days_to_generate=1):
    """
    Looks into repositories folders (hg_files & git files),
    filters the files to load the json's using a passfilter and calls after
    extraction functions.
    :param logger:
    :param days_to_generate: just a pass by parameter, used in extract json
    from git/hg and generates for the specified days.
    :param path_to_files: Folder to json files
    """
    successfully_generated = "part from main markdown table was " \
                             "successfully generated."
    # Get current folder path.
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Look into repositories folder and list all of the files
    only_files = [f for f in listdir(dir_path + "/{}".format(path_to_files)) if
                  isfile(join(dir_path + "/{}".format(path_to_files), f))]
    # Pass filter only the ".json" objects
    json_files = [jf for jf in only_files if ".json" in jf]
    # Extract data from json_files and writes to main markdown table.
    if path_to_files == "git_files":
        extract_json_from_git(json_files, path_to_files, days_to_generate)
        if logger:
            print("GIT" + successfully_generated)
    elif path_to_files == "hg_files":
        extract_json_from_hg(json_files, path_to_files, days_to_generate)
        if logger:
            print("HG" + successfully_generated)

    else:
        if logger:
            print("No table was generated!")
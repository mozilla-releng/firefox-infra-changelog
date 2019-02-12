import re
from datetime import datetime


def compare_files(first_list, second_list):
    """
    Helper Function!
    Compares two lists that should contain the path + filename of the modified files. The two lists
    are mutable.
    :param first_list: First lists.
    :param second_list:  Second list
    :return: returns boolean value in case a match is found.
    """
    for element_f in range(len(first_list)):
        for element_s in range(len(second_list)):
            if str(second_list[element_s]) in str(first_list[element_f]):
                return True
    return False


def clear_file(file_name, generated_for_days=1):
    """
    Helper function.
    This function takes a file that clears the content and output's a base table header for a
    markdown file.
    :param generated_for_days: used for generate the title (default being set for one day)
    :param file_name: Name of the file to be written. (should also contain the path)
    :return: A file should be created and should contain base table.
    """
    file = open(file_name, "w")
    if generated_for_days == 1:
        heading = "##  Commits in production - for one day" + ", generated on: " \
                  + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) + " UTC."
    else:
        heading = "##  Commits in production - for " + \
                  str(generated_for_days) + " days" + ", generated on: " \
                  + str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")) + " UTC."
    file.write(heading)
    file.close()


def get_commit_details(commit):
    """
    Helper function.
    Extracts sha, url, commiter name, commiter email, commiter message, commit date and
    files_changed from a commit object and stores them in a dictionary that gets returned at the
    end.
    :param commit: commit object that should contain information about commit.
    :return: a dictionary with extracted data, properly formatted.
    """
    author_info = {}
    files_changed = []
    try:
        commit_sha = commit.sha
    except ValueError:
        commit_sha = "null"
    try:
        commiter_name = commit.author.login
    except ValueError:
        commiter_name = "null"
    try:
        commiter_email = commit.committer.email
    except ValueError:
        commiter_email = "null"
    try:
        commit_message = commit.commit.message
        commit_message = re.sub("[*\n\r]", " ", commit_message)
    except ValueError:
        commit_message = "null"
    try:
        commit_html_url = commit.html_url
    except ValueError:
        commit_html_url = "null"
    try:
        for entry in commit.files:
            files_changed.append(entry.filename)
    except ValueError:
        pass
    try:
        commit_date = commit.commit.author.date
    except ValueError:
        commit_date = "null"

    author_info.update({"sha": commit_sha,
                        "url": commit_html_url,
                        "commiter_name": commiter_name,
                        "commiter_email": commiter_email,
                        "commit_message": commit_message,
                        "commit_date": str(commit_date),
                        "files_changed": files_changed
                        })
    return author_info


def extract_email(commit_email):
    """
    Helper function!
    Takes as parameter a string that contains between "<" and ">" an email that needs to be
    extracted.
    The function uses find to search for the beginning of the email (that starts with "<") and adds
    the lengths of the "<" so that returned email doesn't contain the "<" symbol and rfind to find
    the ending character ">".
    Both find and rfind return the index where the carachters "<" and ">" are placed so when you do
    return commit_email with [start_char_index:ending_char_index] the string shrinks to what's
    between the characters.
    :param commit_email: String that contains an email
    :return: String that contains only the email
    """
    return commit_email[commit_email.find("<") + len("<"):commit_email.rfind(">")]


def extract_reviewer(string):
    """
    Helper function!
    Takes the string on the input and looks for a specific set of characters (either "r=" or "a=").
    If at least one of them are present (most of the times they are in the mercurial world) then
    this function will return the reviewer/approved by names.
    If none of them are present, the function will return an empty string.
    :param string: usually the commit message.
    :return: a string that may contain the author name (if "r=" or "a=" exists)
    """
    reviewer = ""
    approved_by = ""
    try:
        reviewer = string.split("r=")[1].split()[0]
    except IndexError:
        pass
    try:
        approved_by = string.split("a=")[1].split()[0]
    except IndexError:
        pass

    if len(reviewer) < 1:
        return approved_by
    else:
        return reviewer


def remove_chars(string, char):
    """
    Helper function!
    Removes a specific character from a string
    :param string: string that contains a special char
    :param char: char to be removed from string
    :return: returns a string without char.
    """
    return re.sub(char, " ", string)


def filter_strings(string):
    """
    Helper function!
    Filters the provided string and removes specific words/characters from it that are stored in
    unwanted_chars variable.
    This filter removes chars that can't be written to the markdown file (since the encoding of
    those is not supported).
    :param string: string to be filtered
    :return:
    """
    unwanted_chars = ["\u0131", "\u30c4", "\u00c1", "\u00ee", "\u0103",
                      "\u00e4", "\u00e8", "\u2013", "\U0001f60b", "\u00af",
                      "\U0001f92a"]

    for word in string:
        if word in unwanted_chars:
            string = remove_chars(string, word)

    return string


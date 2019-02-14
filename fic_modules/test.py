def json_writer_hg(repository_name, new_commits):
    """
    :param repository_name:
    :param new_commits: a dictionary with the new commits
    :return: write the json file with the old and the new commits
    """
    hg_json_filename = "{}.json".format(repository_name)
    try:
        with open(WORKING_DIR + "/hg_files/" + hg_json_filename, "r") as \
                commit_json:
            json_content = json.load(commit_json)
    except FileNotFoundError:
        json_content = ""
    #if len(json_content) > 1:
    number = len(new_commits) - 1
    for old_commit in json_content:
        if old_commit == "0":
            json_content["0"] = json_content[old_commit]
        else:
            if json_content[old_commit].get("changeset_commits"):
                number += 1
                json_content.update({int(number): json_content[old_commit]})

    if new_commits :
        json_file = open(WORKING_DIR + "/hg_files/" + hg_json_filename, "w")
        json.dump(new_commits, json_file, indent=2)
        json_file.close()
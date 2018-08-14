import requests
import json
import markdown
import re

git_logs=open('./github_changelog.json').read()
git_data = json.loads(git_logs)
hg_logs=open('./hg_changelog.json').read()
hg_data = json.loads(hg_logs)

f = open('./changelog.md', "a")

changelogs_hg = {}
changelogs_git = {}
changelogs = {}
title = "### GIT" + "\n"
header = "| Repository | Commiter | Email | Time | URL | Message |" + "\n" + "| --- | --- | --- | --- | --- | --- |" + "\n"

f.write(title)
f.write(header)
for key in git_data:                       
    git_repo = {}
    repository = key
    for keys in git_data[key]: 
        commiter_name = git_data[key][keys]['Name: ']
        commiter_email = git_data[key][keys]['Email: '] 
        commit_date = git_data[key][keys]['Date: '] 
        commit_url = git_data[key][keys]['Url: '] 
        commit_message = git_data[key][keys]['Message: ']
        #row_line = ('|' + repository + '|' + commiter_name + '|' + commiter_email + '|' + commit_date + '|' + commit_url + '|' + '\n')
        row_line = ('|' + repository + '|' + commiter_name + '|' + commiter_email + '|' + commit_date + '|' + commit_url + '|' + commit_message + '|' + '\n')
        f.write(row_line)
    
title = "### Mercurial" + "\n"
header = "| Repository | Commiter | Time | Node | Message |" + "\n" + "| --- | --- | --- | --- | --- |" + "\n"

f.write(title)
f.write(header)
for key1 in hg_data:
    hg_repo = {}
    repository = key1
    for keys1 in hg_data[key1]:
        commiter_name = hg_data[key1][keys1]['Name: ']
        commit_date = hg_data[key1][keys1]['Date: ']
        commit_message = hg_data[key1][keys1]['Message: ']
        commt_node = hg_data[key1][keys1]['Node: ']
        #row_line = ('|' + repository + '|' + commiter_name + '|' + commit_date + '|' + commt_node + '|' + '\n')
        row_line = ('|' + repository + '|' + commiter_name + '|' + commit_date + '|' + commt_node + '|' + commit_message + '|' '\n')
        f.write(row_line)
    
        '''commiter_name = data[key][keys]['Name: ']
        print("[{}]".format(commiter_name)"({})".format("profile of commiter") )
        print("| Time | SHA | Commit Msg | Committed by | Repository | Product | Component |")
        print("| --- | --- | --- | --- | --- | --- | --- |")
| commit_date_time | commit_sha | commiter_name | commit_message | [Release Warrior](https://github.com/mozilla-releng/releasewarrior-2.0) | Desktop | Cloud-Tools |
| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [Build Puppet](https://github.com/mozilla-releng/build-puppet) | Desktop | Cloud-Tools |
| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [OpenCloudConfig](https://github.com/mozilla-releng/OpenCloudConfig) | Desktop | Cloud-Tools |
| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [BB Configs](https://github.com/mozilla-releng/build-buildbot-configs) | Desktop | Cloud-Tools |
'''
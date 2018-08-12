import requests
import json
import pprint

git_logs=open('./github_changelog.json').read()
git_data = json.loads(git_logs)
hg_logs=open('./hg_changelog.json').read()
hg_data = json.loads(hg_logs)

changelogs_hg = {}
changelogs_git = {}
changelogs = {}

for key in git_data:                       
    git_repo = {}
    for keys in git_data[key]: 
        git_repo.update( { keys : [git_data[key][keys]['Name: '],
                                   git_data[key][keys]['Email: '],
                                   git_data[key][keys]['Date: '],
                                   git_data[key][keys]['URL: '],
                                   git_data[key][keys]['Message: ']] } )
    changelogs_git.update({ key : git_repo })

for key1 in hg_data:
    hg_repo = {}
    for keys1 in hg_data[key1]:
        hg_repo.update( { keys1 : [hg_data[key1][keys1]['Name: '],
                                   hg_data[key1][keys1]['Date: '],
                                   hg_data[key1][keys1]['Message: '],
                                   hg_data[key1][keys1]['Node: ']]} )
    changelogs_hg.update( { key1: hg_repo} )

changelogs = { 'Git: ' : changelogs_git,
               'Mercurial: ' : changelogs_hg }

with open('./changelog.json', 'w') as fp:
    json.dump(changelogs, fp)

      
        #commiter_name = data[key][keys]['Name: ']
        #print("[{}]".format(commiter_name)"({})".format("profile of commiter") )
        #print("| Time | SHA | Commit Msg | Committed by | Repository | Product | Component |")
        #print("| --- | --- | --- | --- | --- | --- | --- |")
#| commit_date_time | commit_sha | commiter_name | commit_message | [Release Warrior](https://github.com/mozilla-releng/releasewarrior-2.0) | Desktop | Cloud-Tools |
#| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [Build Puppet](https://github.com/mozilla-releng/build-puppet) | Desktop | Cloud-Tools |
#| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [OpenCloudConfig](https://github.com/mozilla-releng/OpenCloudConfig) | Desktop | Cloud-Tools |
#| 07/13/2018 - 20:30 | 86fbbd2df71d | Danut Labici | The best commit that fixes all bugs | [BB Configs](https://github.com/mozilla-releng/build-buildbot-configs) | Desktop | Cloud-Tools |

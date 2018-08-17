import requests
import json
import re

reposLIST = {'shipit': 'https://api.github.com/repos/mozilla-releng/ship-it/commits',
            'services': 'https://api.github.com/repos/mozilla/release-services/commits',
            'beetmoverscript': 'https://api.github.com/repos/mozilla-releng/beetmoverscript/commits',
            'addonscript': 'https://api.github.com/repos/mozilla-releng/addonscript/commits',
            'shipitv2': 'https://api.github.com/repos/mozilla-releng/shipit-v2/commits',
            'build-cloud-tools': 'https://api.github.com/repos/mozilla-releng/build-cloud-tools/commits',
            'build-puppet': 'https://api.github.com/repos/mozilla-releng/build-puppet/commits',
            'shipitscript': 'https://api.github.com/repos/mozilla-releng/shipitscript/commits',
            'bouncerscript': 'https://api.github.com/repos/mozilla-releng/bouncerscript/commits',
            'treescript': 'https://api.github.com/repos/mozilla-releng/treescript/commits',
            'mozapkpublisher': 'https://api.github.com/repos/mozilla-releng/mozapkpublisher/commits',
            'OpenCloudConfig': 'https://api.github.com/repos/mozilla-releng/OpenCloudConfig/commits',
            'scriptworker': 'https://api.github.com/repos/mozilla-releng/scriptworker/commits',
            'pushsnapscript': 'https://api.github.com/repos/mozilla-releng/pushsnapscript/commits',
            'signingscript': 'https://api.github.com/repos/mozilla-releng/signingscript/commits',
            'cot-gpg-keys': 'https://api.github.com/repos/mozilla-releng/cot-gpg-keys/commits',
            'pushapkscript': 'https://api.github.com/repos/mozilla-releng/pushapkscript/commits',
            'balrogscript': 'https://api.github.com/repos/mozilla-releng/balrogscript/commits',
            'funsize': 'https://api.github.com/repos/mozilla-releng/funsize/commits',
            'signtool': 'https://api.github.com/repos/mozilla-releng/signtool/commits'
}  
for reposLIST_key in reposLIST:     # for loop to scroll through the reposLIST
    r = requests.get(reposLIST.get(reposLIST_key))     # get infos from gitAPI page
    p = r.json()     # turn into JSON content 
    commit = {}     # dictionary with key = commit_number and values = name, email, date, URL, message
    commit_number = 0    # commit number initialization
    for keys in p:    # loop to scroll through json content
        author = {}    # dictionary with personal infos about commiter and commit
        commiter_name = keys['commit']['author']['name'] 
        commiter_name = re.sub('[îă]', ' ', commiter_name)   #remove the unrecognized characters from commiter name
        commiter_email = keys['commit']['author']['email'] 
        commit_date = keys['commit']['author']['date'] 
        commit_url = keys['commit']['url'] 
        commit_message = keys['commit']['message']
        message = re.sub('[*\n\r]', ' ', commit_message)  #remove the unrecognized characters from commit message
        author.update({ 'Name: ' : commiter_name,           #add the information about commit and commiter into author dictionary
                        'Email: ' : commiter_email,
                        'Date: ' : commit_date,
                        'Url: ' : commit_url,
                        'Message: ' : message })
        commit.update({ commit_number : author })  #add all the infos from author dictionary into commit dictionary
        commit_number += 1  #increase the commit number
    reposLIST.update({reposLIST_key : commit})     # add all the info into the main dictionary
with open('./github_changelog.json', 'w') as fp:     # open .json file with write permission
    json.dump(reposLIST, fp)     # write in the .json file as a string



''' Using this Json viewer " http://www.jsonviewer.com/ ", 
        you can copy the content from github_changelog.json into RAW json data: 
            and see all the commits '''

   
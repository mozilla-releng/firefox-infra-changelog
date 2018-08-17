import requests
import json
import datetime
import re

hgREPO = { 'Version-Control-Tools' : 'https://hg.mozilla.org/hgcustom/version-control-tools/json-log',
           'Mozilla-Build' : 'https://hg.mozilla.org/mozilla-build/json-log',
           'Tooltool' : 'https://hg.mozilla.org/build/tools/json-log',
           'Mozilla-Central' : 'https://hg.mozilla.org/mozilla-central/json-log',
           'Try' : 'https://hg.mozilla.org/try/json-log',
           'Autoland' : 'https://hg.mozilla.org/integration/autoland/json-log',
           'Inbound' : 'https://hg.mozilla.org/integration/mozilla-inbound/json-log',
           'comm-esr60' : 'https://hg.mozilla.org/releases/comm-esr60/json-log',
           'Beta' : 'https://hg.mozilla.org/releases/mozilla-beta/json-log',
           'mozilla-esr60' : 'https://hg.mozilla.org/releases/mozilla-esr60/json-log',
           'mozilla-release' : 'https://hg.mozilla.org/releases/mozilla-release/json-log'
}

for hgREPO_key in hgREPO:     # for loop to scroll through the hgREPO
    r = requests.get(hgREPO.get(hgREPO_key))     # get infos from hgAPI page
    p = r.json()     # turn into JSON content 
    changelog = {} #dictionary with key= commit number and value= information about commit and commiter
    commit_number = 0 #initialized the commit number with 0 
    for keys in p['changesets']:  #for loop to scroll through json content
        commit = {}  #dictionary to store each  name, date, message and node from each commit
        timestamp = keys['date'][0] 
        value = datetime.datetime.fromtimestamp(timestamp) 
        commit_date = value.strftime('%Y-%m-%d %H:%M:%S') #convert date-time from UNIX to readable format
        commiter_name = keys['user']
        commiter_name = re.sub('[îă]', ' ', commiter_name) #remove the unrecognized characters from commiter name
        commit_message = keys['desc']
        message = re.sub('[*\n\r]', ' ', commit_message)  #remove the unrecognized characters from commit message
        commit_node = keys['node']
        commit.update({ 'Name: ' : commiter_name,   #add the name, date , message and node into commit dictionary
                        'Date: ' : commit_date,
                        'Message: ' : message,
                        'Node: ' : commit_node })
        changelog.update({ commit_number : commit })   #add each info abotu each commit into changelog dictionary
        commit_number += 1 #increase the commit number
    hgREPO.update({ hgREPO_key : changelog}) #add all infos into the main dictionary
with open('./hg_changelog.json', 'w') as fp:     # open .json file with write permission
    json.dump(hgREPO, fp)  #write into JSON file as a string

''' Using this Json viewer " http://www.jsonviewer.com/ ", 
        you can copy the content from github_changelog.json into RAW json data: 
            and see all the commits Radu Iman'''

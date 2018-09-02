#!/bin/bash

python ../tests/git_api.py
sleep 60
echo "Git JSON is ready."
python ../tests/hg_api.py
sleep 60
echo "Mercurial JSON is ready."
python ../tests/json_changelog.py
sleep 60
echo "JSON changelog is ready"
python ../tests/md_changelog.py
sleep 60 
echo "MD changelog is ready."
diff NEW_changelog.md OLD_changelog.md >> changes.md
sleep 30
cat NEW_changelog.md > OLD_changelog.md
echo "DONE"
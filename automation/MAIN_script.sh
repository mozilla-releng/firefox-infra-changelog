#!/bin/bash

python ../tests/git_api.py
echo "Git JSON is ready."
python ../tests/hg_api.py
echo "Mercurial JSON is ready."
python ../tests/json_changelog.py
echo "JSON changelog is ready"
python ../tests/md_changelog.py
echo "MD changelog is ready."
echo "DONE"
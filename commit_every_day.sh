#!/bin/bash
cd ~/projects/kb/ || exit
git add .
FILE_NAME_WITH_PATH=$(git status --porcelain | sed s/^...// | head -n 1)
FILE_NAME="$(basename "$FILE_NAME_WITH_PATH" | sed 's/\(.*\)\..*/\1/')"
echo $FILE_NAME
git commit -m "$FILE_NAME" $FILE_NAME_WITH_PATH
git push -f
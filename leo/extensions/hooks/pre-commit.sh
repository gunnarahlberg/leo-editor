#!/bin/sh

# Move this file to leo-editor/.git/hooks/pre-commit.
# The file must be named pre-commit, NOT pre-commit.sh
 
# http://stackoverflow.com/questions/3878624/how-do-i-programmatically-determine-if-there-are-uncommited-changes
 
if git diff-index --cached --quiet HEAD --ignore-submodules -- ; then
    echo Version info script sees nothing to do
    exit
fi
 
cat >leo/core/commit_timestamp.json << EOT
{
    "asctime": "$(date)",
    "timestamp": "$(date '+%Y%m%d%H%M%S')"
}
EOT
 
echo Updating version info
sleep 1
git add leo/core/commit_timestamp.json

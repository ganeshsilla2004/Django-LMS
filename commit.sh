#!/bin/zsh

# Enter the commit message
echo "Enter the commit message : "
read commit_message

# Enter the branch name
echo "Enter the branch name : "
read branch_name

# adding the commits
git add .

# commit the message
git commit -m "$commit_message"

# push it
git push origin "$branch_name"

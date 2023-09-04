#!/bin/zsh

# Enter the commit message
echo "Enter the commit message : "
read commit_message

# Enter the branch name
echo "Enter the branch name : "
read branch_name

# Enter the remote name 

echo "Enter the remote name : "
read remote_name

# adding the commits
git add .

# commit the message
git commit -m "$commit_message"

# push it
git push "$remote_name" "$branch_name"

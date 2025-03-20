# Setting up in local Machine

## Step-1:

Go to Directory which you want to add in the github

```bash
git init

# It will watch the initalized repo.
```

## Step-2:

Check the status of the repo

```bash
git status

# Tracked files are files which are staged (By git add <filename>) but not commited.
# Untracked files are which are present in the directory, but not staged for commit.
```

## Step-3:

Add files into the repo and check status

```bash
git add <filename> or --all # to add all files 
git status
```

## Step-4:

After finishing our work, we move from `stage` to `commit` of our repo.
When we `commit`, we should always include a message.

```bash
git commit -m "Message for commit"
```

# To Github Server

## Step-1:

Go to Github and copy the repo link `https://github.com/user-name/reponame.git`

```bash
git remote add origin https://github.com/bathula-sharath/OB.git
# git remote add origin URL specifies that you are adding a remote repository, with the specified URL, as an origin to your local Git repo.

git push --set-upstream origin master
# For the 1st Time
```

All the files are uploaded in Github.

## Step-2:

1: Add, modify or delete files then stage for commit => `git add <files> `
2: Commit the Changes => `git commit -m "Message about action" `
3: Push the Changes to remote server => `git push `







================================================================================================
git config --global user.name "bathula-sharath"
git config --global user.email "bathulasharath006@gmail.com"
git config --list


Quick setup — if you’ve done this kind of thing before
https://github.com/bathula-sharath/OB.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line

echo "# OB" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/bathula-sharath/OB.git
git push -u origin main

# cicd_testify
Test repository

# Table of content
- Installation
- Git clone
- Git Push
- Git Pull
- Pull Request, Code review & Merge
- GitHub Actions

## Installation
How to install git 
- Visit https://git-scm.com/downloads
- Select your OS (linux, windows, mac etc)

Create an account on Github
- Signup at https://github.com

## Cloning a Repository on github to your local device
- create a repo on your github account that contains the gitignore, licence and README files
- copy the repo url and either open a terminal on IDE (vscode) then input the command git clone <url> or create a folder on your desktop, open folder on IDE and enter the command in terminal

## Push your changes from your local machine to your github account
- create a new file eg main.py and push it to a new branch eg udeme-dev
- The command to push is git push origin <branch name>

## Pull code from a branch into another branch
- Use the command git checkout <branch name> to switch into the new branch where you intend to pull fresh code into
- Use the command git pull origin <branch with updated code>
- Use the command git push origin <branch to be updated>

## Pull Request (PR) 
This involves asking the project maintainer to review your updates before it is merged to the main or dev branch. PRs can also be created for branch to branch review of code.
- click on the compare and create PR button
- follow th instructions to merge changes from 1 branch to the other
Alternatively,
- click on pull request tab of your repo
- click on the new pull request button
- select the branches you want to merge (base is the destination branch & compare is the branch where changes are to be added from)
- click on create new pull request, enter decription and click create pull request

- Add new comments during code review of a PR is done by clicking on the file changes tab and inputing comment in the section

## Github Actions
- Github Actions allows you test, build and deploy your project from github
- To setup github actions, create a .github/workflows folder if 1 doesnt exist already
- create a .yaml file for the workflow execution
- yaml is a mockup language for configuration files

### NOTICE
- git branch // This will show you the current branch on githib you are currently on
- git branch <branch name> // This takes you (switches) to the branch name inputed
- git checkout <branch name> // This takes you into the branch

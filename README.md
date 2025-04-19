# GIT BRANCH

We can use a copy workspace to work on project without disrupt it.
Just use version of project which works well on main branch,
and use dev branch while you are trying to develop new feature
staging branch is the test branch before release the project
deploy branch is for releasement.

- List branches
``` bash
    git branch 
```

- Create new branch (copy the current branch with current commit) (Use feat/feat-name for features) 
``` bash
    git branch <new-branch-name>
    git branch -M main (for main branch)
```

- Switch to another branch (switch and restore are child commands that split off from checkout command)
``` bash
    git switch <branch-name>
    git checkout <branch-name> 
```

- Merge a branch to the current branch
``` bash
    git merge <other-branch-name>
```

- To rename the current branch
``` bash
    git branch -m <newname>
```


- To rename a branch while pointed to any branch (-m is short for --move)
``` bash
git branch -m <oldname> <newname>
```

- To edit last commit message
``` bash
    git commit --amend -m "New commit message"
```
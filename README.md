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

``` bash
```
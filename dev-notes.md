
# design TODOs
- decide on the minimal repo file structure
- for each scenario, set up a local and remote repo
- create a minimal realistic example of a merge conflict that can be applied to any file in any pair of repos
- define common operations that involve multiple git commands (e.g., add-and-commit)

# infra todos
- add type hints, mypy config, add mypy to pre-commit etc


# troublesome real-world scenarios
## force-pushing to a shared branch
A remote repo with an existing dev branch is cloned by two developers. Their local dev branches diverge after each contributes a few new and different commits to the dev branch. One of them rebases the dev branch and then force pushes the rebased branch, with their changes included, to the remote. How can the second developer update their local dev branch after the rebase, incorporate the first developer's changes, and then contribute their own changes?

### updating local remote-tracking branches after force-pushed changes
A remote repo is cloned on a prod server and an existing `prod` branch is checked out. Later, bug fixes are made in a local dev repo and committed directly to main. The local `prod` branch is rebased on main and then force-pushed to the remote. How can the prod server's remote-tracking `prod` branch be updated to reflect the force-pushed changes? The intuitive answer might be to use `git pull --force` (assuming it to behave symmetrically as `git push --force`) but this does not work as expected - it ends up generating a merge commit. 

### merging the same commits twice
There are two major feature branches, A and B. Suppose a change on A is required to make progress on B, so B is rebased on A *or* one specific commit is cherry-picked from A to B. Development on both branches then continues. At some point, A is merged to main. Later, B is also merged to main. What happens to the commits originally on A that were 'added' on B (by either rebasing or cherry picking)? 

# conceptual questions/issues
### Remote-tracking branches
How are these different from 'normal' local branches, and how can they be set up manually (e.g. without using `git push --set-upstream`)?

### Rebasing nomenclature
How is 'ours' and 'theirs' (or, in vs code, 'current' and 'incoming') defined when rebasing with `--onto`?

### 'Moving' branches
Branches are just pointers to commits, so what's the best way to 'move' a pointer to a different commit? Is there a manual way to do this by editing some internal git object?

### Examples illustrating usage and pitfalls of git reset, checkout, switch, and restore
The context is that git reset and git checkout were too overloaded, so git switch and git restore were introduced. 

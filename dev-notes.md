
# complex or troublesome scenarios

### merging force-pushed changes
A remote repo is cloned on a prod server and an existing `prod` branch is checked out. Later, bug fixes are made in a local dev repo and committed directly to main. The local `prod` branch is rebased on main and then force-pushed to the remote. How can the prod server's remote-tracking `prod` branch be updated to reflect the force-pushed changes? The intuitive answer might be to use `git pull --force` (assuming it to behave symmetrically as `git push --force`) but this does not work as expected - it ends up generating a merge commit. 

### merging the same commits twice
There are two major feature branches, A and B. Suppose a change on A is required to make progress on B, so B is rebased on A *or* one specific commit is cherry-picked from A to B. Development on both branches then continues. At some point, A is merged to main. Later, B is also merged to main. What happens to the commits originally on A that were 'added' on B (by either rebasing or cherry picking)? 

### 'moving' branches
Branches are just pointers to commits, so what's the best way to 'move' to pointer to a different commit?

### Examples illustrating usage and pitfalls of git reset, checkout, switch, and restore
The context is that git reset and git checkout were too overloaded, so git switch and git restore were introduced. 

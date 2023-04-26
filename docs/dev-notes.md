# Dev docs/notes

## Design TODOs
- decide on the minimal repo file structure
- for each scenario, set up a local and remote repo
- create a minimal realistic example of a merge conflict that can be applied to any file in any pair of repos
- define common operations that involve multiple git commands (e.g., add-and-commit)

## Infra todos
- add type hints, mypy config, add mypy to pre-commit etc


## Troublesome real-world scenarios
### Updating local remote-tracking branches after force-pushed changes
A remote repo is cloned on a prod server and an existing `prod` branch is checked out. Later, bug fixes are made in a local dev repo and committed directly to main. The local `prod` branch is rebased on main and then force-pushed to the remote. How can the prod server's remote-tracking `prod` branch be updated to reflect the force-pushed changes? The intuitive answer might be to use `git pull --force` (assuming it to behave symmetrically as `git push --force`) but this does not work as expected - it ends up generating a merge commit.


## Conceptual questions/issues
### Cherry-picking a single commit that involves a merge conflict

### Remote-tracking branches
How are remote-tracking branches different from 'normal' local branches? Can they be set up manually (e.g. without using `git push --set-upstream` or `git checkout --track origin/$some_branch`)?

### Rebasing nomenclature
How is 'ours' and 'theirs' (or, in vs code, 'current' and 'incoming') defined when rebasing with `--onto`?

### 'Moving' branches
Branches are just pointers to commits, so what's the best way to 'move' a pointer to a different commit? Is there a manual way to do this by editing some internal git object?

### Examples illustrating usage and pitfalls of git reset, checkout, switch, and restore
The context is that git reset and git checkout were too overloaded, so git switch and git restore were introduced.

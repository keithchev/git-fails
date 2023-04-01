import os
import git


def create_repo(repo_name):
    if not os.path.exists(repo_name):
        os.makedirs(repo_name)

    repo = git.Repo.init(repo_name)
    return repo


def create_file_and_commit(repo, filename, content, message, overwrite=False):
    with open(os.path.join(repo.working_tree_dir, filename), ('w' if overwrite else 'a')) as f:
        f.write(content)

    repo.index.add([filename])
    author = git.Actor("Author Name", "author@example.com")
    repo.index.commit(message, author=author)


def create_branch_and_checkout(repo, branch_name):
    if branch_name not in repo.heads:
        repo.create_head(branch_name)

    repo.heads[branch_name].checkout()

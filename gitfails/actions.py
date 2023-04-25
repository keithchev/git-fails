import os
import git


def create_repo(repo_dirpath):
    if not os.path.exists(repo_dirpath):
        os.makedirs(repo_dirpath)

    repo = git.Repo.init(repo_dirpath)
    return repo


def create_file_and_commit(repo, filename, content, message, overwrite=False):
    with open(
        os.path.join(repo.working_tree_dir, filename), ('w' if overwrite else 'a')
    ) as file:
        file.write(content)

    repo.index.add([filename])
    author = git.Actor("Author Name", "author@example.com")
    repo.index.commit(message, author=author)


def create_branch_and_checkout(repo, branch_name):
    if branch_name not in repo.heads:
        repo.create_head(branch_name)

    repo.heads[branch_name].checkout()

import os
import git


def create_repo(repo_dirpath):
    if not os.path.exists(repo_dirpath):
        os.makedirs(repo_dirpath)

    repo = git.Repo.init(repo_dirpath)
    return repo


def create_file_and_commit(repo, author, filename, content, message, overwrite=False):
    content = content + '\n' if not content.endswith('\n') else content
    with open(
        os.path.join(repo.working_tree_dir, filename), ('w' if overwrite else 'a')
    ) as file:
        file.write(content)

    repo.index.add([filename])
    author = git.Actor(author, f'{author}@some-domain.com')
    repo.index.commit(message, author=author)


def create_branch_and_checkout(repo, branch_name):
    if branch_name not in repo.heads:
        repo.create_head(branch_name)
    repo.heads[branch_name].checkout()

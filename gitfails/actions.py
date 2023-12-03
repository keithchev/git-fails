import os
import git


def create_repo(repo_dirpath):
    if not os.path.exists(repo_dirpath):
        os.makedirs(repo_dirpath)

    repo = git.Repo.init(repo_dirpath)
    return repo


def create_branch_and_checkout(repo, branch_name):
    if branch_name not in repo.heads:
        repo.create_head(branch_name)
    repo.heads[branch_name].checkout()


def commit_file(repo, author, filename, message):
    repo.index.add([filename])
    author = git.Actor(name=author, email=f'{author}@some-domain.com')
    repo.index.commit(message, author=author)


def create_file_and_commit(repo, author, filename, content, message):
    '''
    create a new file and commit it
    '''
    if filename.exists():
        raise ValueError(f'File {filename} already exists')

    if not content.endswith('\n'):
        content += '\n'

    with open(os.path.join(repo.working_tree_dir, filename), 'w') as file:
        file.write(content)

    commit_file(repo, author, filename, message)


def modify_file_and_commit(repo, author, filename, content, message, overwrite=False):
    '''
    modify an existing file (by either appending to or overwriting it)
    and commit the change
    '''
    if not filename.exists():
        raise ValueError(f'File {filename} does not exist')

    mode = 'w' if overwrite else 'a'
    with open(os.path.join(repo.working_tree_dir, filename), mode) as file:
        file.write(content)

    commit_file(repo, author, filename, message)

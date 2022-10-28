import git
import pathlib
import os


class Repo:

    def __init__(self, dirpath):

        self.repo = git.Repo.init(dirpath, mkdir=True)


    def add_and_commit(self, filepath, content, message, replace=None, overwrite=False):
        '''
        filepath : path to the file to replace (relative to the repo directory)
        content : content to write
        message : commit message
        replace : content to replace with `content`
        overwrite : whether to overwrite the file completely

        '''
        filepath = pathlib.Path(self.repo.working_dir) / 'readme.md'
        with open(filepath, ('w' if overwrite else 'a')) as file:
            file.write('Hello world')

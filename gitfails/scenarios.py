import abc
import os
import shutil

from gitfails import utils
from gitfails.actions import create_branch_and_checkout, create_file_and_commit, create_repo


class Scenario(abc.ABC):
    def __init__(self, dirpath, overwrite=False):
        self.dirpath = dirpath
        if overwrite:
            if os.path.exists(self.dirpath):
                shutil.rmtree(self.dirpath)

    def __repr__(self):
        return f'<Scenario {self.name}>'

    @abc.abstractmethod
    def construct():
        raise NotImplementedError


class TwoFeatureBranches(Scenario):
    '''
    A git repo with a `main` branch and two feature branches, A and B.

    Suppose a commit on A is required to make progress on B,
    so either B is rebased on A, or the commit is cherry-picked from A to B.
    Development on both branches then continues, until A is merged to main.

    When B is eventually merged to main, what happens to the commits originally on A
    that were 'added' on B (by either rebasing or cherry picking)?
    '''

    def construct(self):
        ''' '''
        repo_dirpath = self.dirpath / 'repo'
        repo = create_repo(repo_dirpath)

        # create a file on the main branch and commit
        create_file_and_commit(repo, "file1.txt", "Initial content\n", "Initial commit")

        # create branch A, add a file, and commit
        create_branch_and_checkout(repo, "A")
        create_file_and_commit(
            repo, "file2.txt", "Content for branch A\n", "Commit on branch A"
        )

        # switch back to main, create branch B, add a file, and commit
        create_branch_and_checkout(repo, "main")
        create_branch_and_checkout(repo, "B")
        create_file_and_commit(
            repo, "file3.txt", "Content for branch B\n", "Commit on branch B"
        )

        # switch back to the main branch
        create_branch_and_checkout(repo, "main")


class RecoverFromPushForce(Scenario):
    def construct(self):
        pass


scenario_classes = {
    ScenarioSubclass.__name__: ScenarioSubclass
    for ScenarioSubclass in Scenario.__subclasses__()
}

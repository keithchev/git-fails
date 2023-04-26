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

    @abc.abstractmethod
    def construct(self):
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
        create_file_and_commit(
            repo, filename='file1.txt', content='Initial content\n', message='Initial commit'
        )

        # create branch A, add a file, and commit
        create_branch_and_checkout(repo, 'A')
        create_file_and_commit(
            repo,
            filename='file2.txt',
            content='Content from branch A\n',
            message='Commit on branch A',
        )

        # switch back to main, create branch B, add a file, and commit
        create_branch_and_checkout(repo, 'main')
        create_branch_and_checkout(repo, 'B')
        create_file_and_commit(
            repo,
            filename='file3.txt',
            content='Content from branch B\n',
            message='Commit on branch B',
        )

        # switch back to the main branch
        create_branch_and_checkout(repo, 'main')


class ForcePushSharedBranch(Scenario):
    '''
    A remote repo with an existing dev branch is cloned by two developers.
    Their local dev branches diverge after each makes new commits to their local dev branches.
    One of them rebases their local dev branch on main and then force pushes to the remote.

    How can the second developer update their local dev branch after the rebase
    to incorporate the first developer's changes, and then contribute their own changes?
    '''

    def construct(self):

        # set up the remote/origin repo
        origin_repo = create_repo(self.dirpath / 'origin')
        create_file_and_commit(
            origin_repo,
            filename='file1.txt',
            content='Initial content\n',
            message='Initial commit to main',
        )
        create_file_and_commit(
            origin_repo,
            filename='file1.txt',
            content='Modified content\n',
            message='Second commit to main',
            overwrite=True,
        )

        # clone the origin repo to represent the good and bad dev repos
        bad_dev_repo = origin_repo.clone(self.dirpath / 'bad_dev')
        good_dev_repo = origin_repo.clone(self.dirpath / 'good_dev')

        # create a branch on the bad-dev repo and push it to the origin
        create_branch_and_checkout(bad_dev_repo, 'dev')
        create_file_and_commit(
            bad_dev_repo,
            filename='file2.txt',
            content='Change from the bad-dev repo\n',
            message='Commit from the bad-dev',
        )
        bad_dev_repo.remotes.origin.push('dev')

        # create a new commit directly on `main` in the origin
        # (this represents ongoing changes from, e.g., merged PRs)
        create_file_and_commit(
            origin_repo,
            filename='file1.txt',
            content='Modified content again\n',
            message='Third commit to main',
            overwrite=True,
        )

        # update the main branch in both dev repos
        good_dev_repo.git.checkout('main')
        good_dev_repo.remotes.origin.pull('main')
        bad_dev_repo.git.checkout('main')
        bad_dev_repo.remotes.origin.pull('main')

        # fetch the dev branch in the good-dev repo and add a new commit (but do not push)
        good_dev_repo.remotes.origin.fetch()
        good_dev_repo.git.checkout('dev')
        create_file_and_commit(
            good_dev_repo,
            filename='file2.txt',
            content='Change from good-dev repo\n',
            message='Commit from the good dev',
        )

        # rebase the dev branch on the updated main branch in the bad-dev repo and force-push it
        bad_dev_repo.git.checkout('dev')
        bad_dev_repo.git.rebase('main')
        bad_dev_repo.remotes.origin.push('dev', force=True)

        # fetch and checkout the dev branch in the good-dev repo,
        # which because of the force-push has now diverged from the remote dev branch
        good_dev_repo.remotes.origin.fetch()
        good_dev_repo.git.checkout('dev')


scenario_classes = {
    ScenarioSubclass.__name__: ScenarioSubclass
    for ScenarioSubclass in Scenario.__subclasses__()
}

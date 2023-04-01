from gitfails.actions import create_repo, create_file_and_commit, create_branch_and_checkout


def two_feature_branches():
    ''' '''
    # Create a new repo
    repo = create_repo("sample_repo")

    # Create a file on the main branch and commit
    create_file_and_commit(repo, "file1.txt", "Initial content\n", "Initial commit")

    # Create branch A, add a file, and commit
    create_branch_and_checkout(repo, "A")
    create_file_and_commit(repo, "file2.txt", "Content for branch A\n", "Commit on branch A")

    # Create branch B, add a file, and commit
    create_branch_and_checkout(repo, "B")
    create_file_and_commit(repo, "file3.txt", "Content for branch B\n", "Commit on branch B")

    # Switch back to the main branch
    create_branch_and_checkout(repo, "main")

import click
import os
import textwrap

from ...utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
commit = CommandGroup(name="commit", help="Help with git commit commands")
BASE_COMMAND = commit


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class CommitSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(commit, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Change author and/or date of an old commit
CommitSubCommand(
    textwrap.dedent("""
        1. Do an interactive rebase and "edit" the commit
        2. When stopped, do 'git commit --amend --author="name <email>
                             --date="Tue Dec 12 2017 09:01:14 -0600"'
    """),
    name="change-author-and-or-date",
    help="Change author and/or date of an old commit",
)

# Remove a specific commit
CommitSubCommand(
    "git rebase -p --onto SHA1^ SHA1",
    name="remove",
    help="Remove a specific commit",
)

# Set author date when committing
CommitSubCommand(
    "git commit -m 'message' --date='Tue Dec 12 2017 09:01:14 -0600'",
    name="set-author-date",
    help="Set author date when creating a commit",
)

# Set commit date when committing
CommitSubCommand(
    'GIT_COMMITTER_DATE="Tue Dec 12 2017 09:01:14 -0600" git commit ' \
        '-m "message"',
    name="set-commit-date",
    help="Set commit date when creating a commit",
)

# Set author when committing
CommitSubCommand(
    "git commit -m 'message' --author='Name <email>'",
    name="set-author",
    help="Set the author when creating a commit",
)

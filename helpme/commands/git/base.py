import click
import os
import textwrap

from ...utils import CommandGroup, SubCommand, get_module


###############################################################################
# Main command ################################################################
###############################################################################
git = CommandGroup(module=get_module(__name__), name="git",
                   help="Help with git commands")
BASE_COMMAND = git


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class GitSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(git, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Add upstream branch to existing local branch
GitSubCommand(
    "git branch -u origin <branch-name>",
    name="add-upstream-branch",
    help="Add upstream branch to existing local branch",
)

# Add upstream branch to existing local branch
GitSubCommand(
    "git remote add upstream <URL>",
    name="add-upstream-repo",
    help="Add an upstream repo",
)

# Pull updates from remote into another branch
GitSubCommand(
    "git fetch origin master:master",
    name="pull-into-another-branch",
    help="Pull a remote into another local branch without switching branches",
)

# Remove upstream branch
GitSubCommand(
    "git branch --unset-upstream",
    name="remove-upstream-branch",
    help="Remove upstream branch from local branch",
)

# Set local repo as remote on another local repo
GitSubCommand(
    "git remote add repo_name /path/to/repo.git",
    name="set-local-repo-as-remote",
    help="Set a git repo on the local filesystem as a remote for another repo",
)

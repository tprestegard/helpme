import textwrap

from ...core import CommandGroup, SubCommand, get_module


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

# Push local branch to remote
GitSubCommand(
    "git push -u origin <branch_name>",
    name="push-local-branch-to-remote",
    help="Push a local git branch to a branch in a remote repo",
)

# Delete a remote branch
GitSubCommand(
    "git push --delete origin <branch-name>",
    name="delete-remote-branch",
    help="Delete a remote branch",
)

# Check out a remote branch locally
GitSubCommand(
    "git checkout --track origin/<branch-name>",
    name="checkout-and-track-remote-branch",
    help="Check out a remote branch locally and track the remote",
)

# Clean up untracked files
GitSubCommand(
    "git clean -dxf",
    name="delete-untracked-files",
    help="Delete untracked files in local repo",
)

# Remove old branches from remote
GitSubCommand(
    "git remote prune origin",
    name="prune-remote-branches",
    help="Delete references to remote branches that no longer exist",
)

# Checkout an upstream branch into a fork
GitSubCommand(
    textwrap.dedent("""
        git fetch upstream
        git checkout -b <branch-name> upstream/<branch-name>
        git push -u origin <branch-name>
    """),
    name="fork-upstream-branch",
    help="Checkout a branch from an upstream repo into a fork",
)

# Search git diffs for any commits which add or remove a string
GitSubCommand(
    "git log -S\"string\"",
    name="search-commits-for-string",
    help="Search git diffs for any commits which add or remove a string",
)

# Search commit messages interactively
GitSubCommand(
    textwrap.dedent("""
        git log
        Use '/string' to search and n/N to navigate down/up
    """),
    name="search-commit-messages",
    help="Search commit messages interactively for a string",
)

# Override local branch with remote
GitSubCommand(
    textwrap.dedent("""
        git fetch --all
        git reset --hard origin/<branch-name>
    """),
    name="override-local-branch",
    help="Override local branch with remote",
)

from ...utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
tags = CommandGroup(name="tags", help="Help with git tags")
BASE_COMMAND = tags


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class TagsSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(tags, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Create a git tag
TagsSubCommand(
    "git tag -a \"version\" -m \"message\"",
    name="create-tag",
    help="Create a tag",
)

# List tags with messages and sorted by version
TagsSubCommand(
    "git tag -l --sort=v:refname -n",
    name="list-tags-sorted-by-version",
    help="List all tags with messages and sorted by version",
)

# Push tags to remote
TagsSubCommand(
    "git push --tags",
    name="push-tags-to-remote",
    help="Push local tags to remote",
)

# Delete a local tag
TagsSubCommand(
    "git tag -d 1.2.1",
    name="delete-local-tag",
    help="Delete a local tag",
)

# Push local tag deletion to remote
TagsSubCommand(
    "git push --delete origin 1.2.1",
    name="delete-tag-on-remote",
    help="Delete tag in remote repo",
)

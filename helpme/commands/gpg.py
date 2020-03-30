import textwrap

from ..utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
gpg = CommandGroup(name="gpg", aliases=["gpg2"], help="Help with gpg commands")
BASE_COMMAND = gpg


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class GpgSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(gpg, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# List secret keys in a format for setting Git settings
GpgSubCommand(
    textwrap.dedent("""
        gpg --list-secret-keys --keyid-format LONG
        # Use value after rsa****/ on line starting with "sec"
    """),
    name="show-keys-for-git",
    help="List secret keys in a format usable for Git settings",
)

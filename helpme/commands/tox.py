import textwrap

from ..utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
tox = CommandGroup(name="tox", help="Help with tox commands")
BASE_COMMAND = tox


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class ToxSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(tox, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################

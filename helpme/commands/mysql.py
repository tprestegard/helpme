import textwrap

from ..utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
mysql = CommandGroup(name="mysql", help="Help with mysql commands")
BASE_COMMAND = mysql


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class MysqlSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(mysql, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
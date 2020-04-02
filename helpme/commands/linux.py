import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
linux = CommandGroup(name="linux", help="Help with generic Linux stuff")
BASE_COMMAND = linux


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class LinuxSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(linux, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Remove configuration files for uninstalled packages
LinuxSubCommand(
    "dpkg --list | grep \"^rc\" | cut -d \" \" -f  | xargs sudo dpkg --purge",
    name="purge-config-files",
    help="Purge configuration files for removed packages",
)

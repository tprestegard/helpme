import textwrap

from ..utils import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
docker_compose = CommandGroup(name="docker-compose",
                              help="Help with docker-compose commands")
BASE_COMMAND = docker_compose


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class DockerComposeSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(docker_compose, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
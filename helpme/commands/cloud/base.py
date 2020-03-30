import textwrap

from ...utils import CommandGroup, SubCommand, get_module


###############################################################################
# Main command ################################################################
###############################################################################
cloud = CommandGroup(module=get_module(__name__), name="cloud",
                     help="Help with cloud-related commands")
BASE_COMMAND = cloud


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class CloudSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(cloud, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Install Google Cloud SDK
CloudSubCommand(
    textwrap.dedent("""
        curl https://sdk.cloud.google.com | bash
        # NOTE: select 'yes' when it asks to add to .bashrc
        gcloud init
        exec -l $SHELL
    """),
    name="install-google-cloud-sdk",
    help="Install Google Cloud SDK"
)

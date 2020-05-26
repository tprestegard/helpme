from ...core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
gcp = CommandGroup(name="gcp", help="Help with GCP")
BASE_COMMAND = gcp


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class GcpSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(gcp, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Get credentials
GcpSubCommand(
    "gcloud compute images list --filter \"name=centos-8\" --uri "
    "--show-deprecated",
    name="get-image-uri",
    help="Look up image URIs",
)

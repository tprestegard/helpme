from ...core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
rsync = CommandGroup(name="rsync", help="Help with rsync commands")
BASE_COMMAND = rsync


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class RsyncSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(rsync, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Rsync to AWS
RsyncSubCommand(
    "# NOTE: set up SSH keys and configure sshd first\n"
    "env SSH_AUTH_SOCK=\"\" rsync -av --delete -e \"ssh -i "
    "/home/tanner/univa/navops-launch/demo/aws/.ssh/navops-launch-demo-tanner"
    ".pem\" . root@ec2-34-213-178-76.us-west-2.compute.amazonaws.com:"
    "/root/image_builder/",
    name="aws",
    help="Rsync folder to AWS for development",
)

# Rsync to Azure
RsyncSubCommand(
    "# NOTE: set up SSH keys and configure sshd first\n"
    "rsync -av --delete -e \"ssh -i /home/tanner/univa/navops-launch/demo/"
    "azure/.ssh/id_rsa\" . root@52.237.39.219:/root/image_builder/",
    name="azure",
    help="Rsync folder to Azure for development",
)

# Rsync to GCP
RsyncSubCommand(
    "# NOTE: set up SSH keys and configure sshd first\n"
    "gcp_rsync <ip-address> . /root/image_builder root",
    name="gcp",
    help="Rsync folder to GCP for development",
)

import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
kubectl = CommandGroup(name="kubectl", help="Help with kubectl commands")
BASE_COMMAND = kubectl


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class KubectlSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(kubectl, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# See all pods
KubectlSubCommand(
    "kubectl get pods",
    name="view-all-pods",
    help="View all pods",
)

# Enter a running container
KubectlSubCommand(
    "kubectl <container-name> -- /bin/bash -l",
    name="enter-container",
    help="Enter a running container",
)

# Follow logs
KubectlSubCommand(
    "kubectl logs -f <container-name>",
    name="follow-logs",
    help="Continuously output logs",
)

# Restart a container
KubectlSubCommand(
    'kubectl patch deployment -n <namespace> <deployment> -p "{\\"spec\\":'
    '{\\"template\\":{\\"metadata\\":{\\"labels\\":{\\"date\\":'
    '\\"`date +\'%s\'`\\"}}}}}',
    name="restart-container",
    help="Restart a running container",
)

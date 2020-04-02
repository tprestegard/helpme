import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
tmux = CommandGroup(name="tmux", help="Help with tmux commands")
BASE_COMMAND = tmux


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class TmuxSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(tmux, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Share a tmux session
TmuxSubCommand(
    "tmux -S /tmp/shareds new -s shared",
    name="create-shared-session",
    help="Start a shared session",
)

# Kill a tmux pane
TmuxSubCommand(
    "Ctrl+b x",
    name="kill-pane",
    help="Kill the current pane",
)

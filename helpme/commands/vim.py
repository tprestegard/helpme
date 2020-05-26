import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
vim = CommandGroup(name="vim", help="Help with vim commands")
BASE_COMMAND = vim


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class VimSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(vim, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Show whitespace
VimSubCommand(
    ":set list",
    name="show-whitespace",
    help="Show whitespace characters",
)

# Show line numbers
VimSubCommand(
    ":set number",
    name="show-line-numbers",
    help="Show line numbers",
)

# Make current word uppercase
VimSubCommand(
    "gUiw",
    name="uppercase-word",
    help="Make current word uppercase",
)

# Make current word lowercase
VimSubCommand(
    "guiw",
    name="lowercase-word",
    help="Make current word lowercase",
)

# Invert case of current word
VimSubCommand(
    "g~iw",
    name="invert-case-word",
    help="Invert case of current word",
)

# Jump to line
VimSubCommand(
    "<line-number>G",
    name="jump-to-line",
    help="Jump to a specified line number",
)

# Open new line after current
VimSubCommand(
    "o",
    name="open-new-line-below",
    help="Create a new line below the current one and enter insert mode",
)

# Open new line before current
VimSubCommand(
    "O",
    name="open-new-line-above",
    help="Create a new line above the current one and enter insert mode",
)

# Copy current line
VimSubCommand(
    "yy",
    name="copy-current-line",
    help="Copy current line",
)

# Run shell command
VimSubCommand(
    textwrap.dedent("""
    :! <command>        Run shell command
    :read ! <command>   Run shell command and copy output into buffer
    :2read ! <command>  Run shell command and copy output after line 2 of
                        buffer
    :! ls -lh %         Get details on current file (%)
    """),
    name="shell-commands",
    help="Help with running shell commands",
)

# Regex
# NERDTree

import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
openssl = CommandGroup(name="openssl", help="Help with openssl commands")
BASE_COMMAND = openssl


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class OpensslSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(openssl, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Generate encrypted file using password
OpensslSubCommand(
    "openssl enc -aes-256-cbc -iter 1000 -in stuff.tar.gz -out "
    "stuff.enc.tar.gz",
    name="encrypt-file-with-password",
    help="Encrypt file with password",
)

# Decrypt file with password
OpensslSubCommand(
    "openssl enc -d -aes-256-cbc -iter 1000 -in stuff.enc.tar.gz -out "
    "stuff.tar.gz",
    name="decrypt-file-with-password",
    help="Decrypt file with password",
)

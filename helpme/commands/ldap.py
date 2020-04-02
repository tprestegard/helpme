import textwrap

from ..core import CommandGroup, SubCommand


###############################################################################
# Main command ################################################################
###############################################################################
ldap = CommandGroup(name="ldap", help="Help with ldap commands")
BASE_COMMAND = ldap


###############################################################################
# Base class for subcommands ##################################################
###############################################################################
class LdapSubCommand(SubCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(ldap, *args, **kwargs)


###############################################################################
# Subcommands #################################################################
###############################################################################
# Query LDAP based on UID
LdapSubCommand(
    "ldapsearch -t -LLL -x -b \"dc=ligo,dc=org\" -H ldaps://ldap.ligo.org "
    "uid=tanner.prestegard",
    name="query-for-uid",
    help="Query LDAP for a specific UID",
)

# Query for all robot accounts
LdapSubCommand(
    "ldapsearch -LLL -x -Z -b \"ou=robot,dc=ligo,dc=org\" -H "
    "ldap://ldap.ligo.org",
    name="query-robot-accounts",
    help="Query LDAP for all robot accounts",
)

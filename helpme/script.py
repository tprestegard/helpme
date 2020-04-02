from .core import CommandGroup, get_module


# Main command
main = CommandGroup(module=get_module(__name__, 'commands'), name="helpme",
                    help="HELP!")

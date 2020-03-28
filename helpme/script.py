import os

from .utils import CommandGroup, get_module


# Main command
main = CommandGroup(module=get_module(__name__, 'commands'), name="helpme",
                    help="HELP!")


#import helpme.commands
#
#@click.group()
#def main():
#    """
#    Help text TBD
#    """
#    pass
#
#
## Load commands
#for finder, name, _ in pkgutil.iter_modules(helpme.commands.__path__,
#                                            helpme.commands.__name__ + "."):
#    main.add_command(importlib.import_module(name).BASE_COMMAND)

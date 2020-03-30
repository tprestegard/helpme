import click
import copy
import importlib
import pkgutil
from typing import List


class PrintCommand(click.Command):
    """Click command that just prints a message"""
    def __init__(self, msg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg.strip()

    def invoke(self, ctx):
        for line in self.msg.split('\n'):
            click.secho(line)


class RegisteredCommandMixin:
    def __init__(self, parent: click.Group, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._register(parent)

    def _register(self, parent: click.Group):
        parent.add_command(self)


class RegisterSubCommandsMixin:
    def __init__(self, *args, module: str = None, **kwargs):
        super().__init__(*args, **kwargs)
        if module:
            self._lookup_module = importlib.import_module(module)
            self._find_and_add_subcommands()
        else:
            self._lookup_module = None

    def _find_and_add_subcommands(self):
        path = self._lookup_module.__path__
        prefix = self._lookup_module.__name__ + "."
        for finder, name, _ in pkgutil.iter_modules(path, prefix):
            if not (name.endswith('base') or name.endswith('base.py')):
                cmd = importlib.import_module(name).BASE_COMMAND
                self.add_command(cmd)

                # Aliases
                if cmd.aliases:
                    for alias in cmd.aliases:
                        # Make a copy and add under the aliased name
                        cmd_copy = copy.deepcopy(cmd)
                        cmd_copy.hidden = True
                        self.add_command(cmd_copy, name=alias)


class AliasMixin:
    def __init__(self, *args, aliases: List[str] = [], **kwargs):
        self.aliases = aliases
        super().__init__(*args, **kwargs)


class CommandGroup(RegisterSubCommandsMixin, AliasMixin, click.Group):
    pass


class SubCommand(RegisteredCommandMixin, AliasMixin, PrintCommand):
    pass


def get_module(current_module: str, relative_module_path: str = None) -> str:
    module_str = current_module.rsplit('.', 1)[0]
    if relative_module_path:
        module_str += f".{relative_module_path}"
    return module_str

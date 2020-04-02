import click
import copy
import importlib
import pkgutil
from typing import List


class RegisteredCommandMixin:
    """Mixin which registers a command or group with a parent group"""
    def __init__(self, parent: click.Group, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._register(parent)

    def _register(self, parent: click.Group):
        parent.add_command(self)


class RegisterSubCommandsMixin:
    """Mixin which registers subcommands or subgroups in a given module"""
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
    """Mixin which saves a list of strings representing command aliases"""
    def __init__(self, *args, aliases: List[str] = [], **kwargs):
        self.aliases = aliases
        super().__init__(*args, **kwargs)

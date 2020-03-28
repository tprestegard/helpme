import click
import importlib
import os
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
        #parent.commands[self.name] = self


class RegisterSubCommandsMixin:
    def __init__(self, *args, module: str=None, **kwargs):
        super().__init__(*args, **kwargs)
        if module:
            self._lookup_module = importlib.import_module(module)
            self._find_and_add_subcommands()
        else:
            self._lookup_module = None

    def _find_and_add_subcommands(self):
        for finder, name, _ in pkgutil.iter_modules(self._lookup_module.__path__, self._lookup_module.__name__ + "."):
            if not (name.endswith('base') or name.endswith('base.py')):
                self.add_command(importlib.import_module(name).BASE_COMMAND)


class CommandGroup(RegisterSubCommandsMixin, click.Group):
    pass


class SubCommand(RegisteredCommandMixin, PrintCommand):
    pass



def get_module(current_module: str, relative_module_path: str=None) -> str:
    module_str = current_module.rsplit('.', 1)[0]
    if relative_module_path:
        module_str += f".{relative_module_path}"
    return module_str


def recursive_cmd(group_or_cmd):
    name = group_or_cmd[0]
    help_msg = group_or_cmd[1]
    msg_or_cmds = group_or_cmd[2]
    if isinstance(msg_or_cmds, (list, tuple)):
        group = click.Group(name=name, help=help_msg)
        for cmd in msg_or_cmds:
            group.add_command(recursive_cmd(cmd))
        return group
    else:
        return PrintCommand(msg_or_cmds, name=name, help=help_msg)

import click

from .mixins import AliasMixin, RegisterSubCommandsMixin


class CommandGroup(RegisterSubCommandsMixin, AliasMixin, click.Group):
    pass

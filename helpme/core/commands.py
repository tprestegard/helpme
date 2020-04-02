from .base import PrintCommand
from .mixins import AliasMixin, RegisteredCommandMixin


class SubCommand(RegisteredCommandMixin, AliasMixin, PrintCommand):
    pass

import click


class PrintCommand(click.Command):
    """Click command that just prints a message"""
    def __init__(self, msg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg.strip()

    def invoke(self, ctx):
        for line in self.msg.split('\n'):
            click.secho(line)



import sys
import logging

import click

from cli.benchmark import benchmark
from cli.summary import summary


log = logging.getLogger()
logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)
logging.getLogger("tools.performance").setLevel(logging.DEBUG)


@click.group(chain=True, context_settings=dict(help_option_names=["-h", "--help"]))
def main():
    pass


main.add_command(benchmark)
main.add_command(summary)


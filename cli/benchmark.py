

import click

#from tools.benchmark import




@click.command("benchmark")
@click.option("-r", "--routing-problem", required=True, help="name of routing problem to benchmark")
def benchmark(routing_problem: str):
    click.echo(forcing_a_transition)
    click.echo(implementation_by_setting_values_of_next_var)
    click.echo(implementation_by_member_ct)

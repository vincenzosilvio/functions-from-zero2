# build a shebang line to run the script
#!/usr/bin/env python3

from mylib.calc import add, subtract, multiply, divide, power, sqrt
import click


@click.group()
def cli():
    pass


@click.command("add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_cmd(x, y):
    click.secho(f"{add(x, y)}", fg="green")


@click.command("divide")
@click.argument("x", type=float)
@click.argument("y", type=float)
def div_cmd(x, y):
    click.secho(f"{divide(x, y)}", fg="green")


# add the other commands here
@click.command("subtract")
@click.argument("x", type=float)
@click.argument("y", type=float)
def sub_cmd(x, y):
    click.secho(f"{subtract(x, y)}", fg="green")


@click.command("multiply")
@click.argument("x", type=float)
@click.argument("y", type=float)
def mul_cmd(x, y):
    click.secho(f"{multiply(x, y)}", fg="green")


@click.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def pow_cmd(x, y):
    click.secho(f"{power(x, y)}", fg="green")


@click.command("sqrt")
@click.argument("x", type=float)
def sqrt_cmd(x):
    click.secho(f"{sqrt(x)}", fg="green")


# invoke it
if __name__ == "__main__":
    cli.add_command(add_cmd)
    cli.add_command(div_cmd)
    cli()

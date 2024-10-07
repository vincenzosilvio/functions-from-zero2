from mylib.logistics import (
    calculate_distance,
    total_distance,
    cities,
    get_coordinates,
    travel_time,
)
import click

# build a click group
@click.group()
def cli():
    pass


# build a click command to list cities'name
@cli.command("cities")
def print_cities():
    """Print a list of cities"""
    click.secho(f"{cities}", fg="green")


# build a click command
@cli.command("distance")
@click.argument("city1", type=str)
@click.argument("city2", type=str)
def calculate_city_distance(city1, city2):
    """Calculate distance between two cities using get_coordinates"""
    click.secho(
        f"{calculate_distance(get_coordinates(city1), get_coordinates(city2))}",
        fg="green",
    )


# build a click command for getting the coordinates of a city
@cli.command("coordinates")
@click.argument("city", type=str)
def get_city_coordinates(city):
    """Get coordinates of a city"""
    click.secho(f"{get_coordinates(city)}", fg="green")


# build a click command for travel time between two cities by car calling the travel_time function
@cli.command("travel")
@click.argument("city1", type=str)
@click.argument("city2", type=str)
@click.option("--speed", default=60, help="Speed in miles per hour")
def travel(city1, city2, speed):
    """Calculate travel time between two cities"""
    click.secho(
        f"{travel_time(city1, city2, speed)} hours",
        fg="green",
    )


# invoke the click group
if __name__ == "__main__":
    cli()

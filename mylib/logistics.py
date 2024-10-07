""""
This module deals with logistics and calculates distance between two points
and the time it takes to travel between two points and other logistics related 
questions for a given speed
"""

from geopy import distance

# build a list of cities and their coordinates (10 cities in the USA)
cities = {
    "Los Angeles": (34.0522, 118.2437),
    "Chicago": (41.8781, 87.6298),
    "Houston": (29.7604, 95.3698),
    "Phoenix": (33.4484, 112.0740),
    "Philadelphia": (39.9526, 75.1652),
    "San Antonio": (29.4241, 98.4936),
    "San Diego": (32.7157, 117.1611),
    "Dallas": (32.7767, 96.7970),
    "San Jose": (37.3382, 121.8863),
    "Austin": (30.2672, 97.7431),
}

# build a function to calculate the distance between two cities
def calculate_distance(city1, city2):
    """
    This function calculates the distance between two cities
    :param city1: str
    :param city2: str
    :return: float
    """
    return distance.distance(city1, city2).miles


def get_coordinates(city):
    """
    This function returns the coordinates of a city
    :param city: str
    :return: tuple
    """
    return cities[city]


# calculate the total distaance between a list of cities
def total_distance(city_list):
    """
    This function calculates the total distance between a list of cities
    :param city_list: list
    :return: float
    """
    total = 0
    for i in range(len(city_list) - 1):
        total += calculate_distance(city_list[i], city_list[i + 1])
    return total


def print_cities():
    """
    This function prints the list of cities
    :return: None
    """
    for city in cities:
        print(city)
    return city[0]


# estimate the travel time between two cities by car
# assume speed is 60 miles per hour
# use get_coordinates and calculate_distance
def travel_time(city1, city2, speed=60):
    """
    This function calculates the travel time between two cities
    :param city1: str
    :param city2: str
    :return: float
    """
    return calculate_distance(get_coordinates(city1), get_coordinates(city2)) / speed

from mylib.logistics import (
    calculate_distance,
    find_coordinates,
    total_distance,
    cities,
    print_cities,
)


def test_distance_between_two_points():
    assert calculate_distance("Los Angeles", "Chicago") == 1745.0
    assert calculate_distance("Los Angeles", "Houston") == 1379.0
    assert calculate_distance("Los Angeles", "Phoenix") == 371.0
    assert calculate_distance("Los Angeles", "Philadelphia") == 2389.0
    assert calculate_distance("Los Angeles", "San Antonio") == 1371.0
    assert calculate_distance("Los Angeles", "San Diego") == 120.0
    assert calculate_distance("Los Angeles", "Dallas") == 1243.0
    assert calculate_distance("Los Angeles", "San Jose") == 308.0
    assert calculate_distance("Los Angeles", "Austin") == 1377.0


def test_print_cities():
    assert print_cities() == cities[0]

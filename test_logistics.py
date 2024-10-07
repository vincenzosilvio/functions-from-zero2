from mylib.logistics import *
from fastapi.testclient import TestClient
from main import app
import pytest
import geopy


def test_distance_between_two_points():
    assert int(calculate_distance(get_coordinates("Chicago"), get_coordinates("Los Angeles"))) == 1745


# build a test for travel_time
# def travel_time(city1, city2, speed=60):
def test_travel_time2():
    hours = travel_time("Chicago", "Los Angeles")
    assert int(hours) == 29


def test_cities_list():
    assert "Dallas" in cities


#### Web Application Testing
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Logistics INC"}


# build a test for the cities endpoint
def test_cities(client):
    response = client.post("/cities")
    assert response.status_code == 200
    assert "cities" in response.json()


# build a test for the distance endpoint for chicago and los angeles
def test_distance(client):
    response = client.post(
        "/distance",
        json={"city1": {"name": "Chicago"}, "city2": {"name": "Los Angeles"}},
    )
    assert response.status_code == 200
    assert response.json() == {"distance": 1745.7680630496661}



# build a test the travel time between two cities by car for Chicago and Los Angeles, consider the speed is 60 miles per hour
def test_travel(client):
    response = client.post(
        "/travel",
        json={
            "city1": {"name": "Chicago"},
            "city2": {"name": "Los Angeles"},
            "speed": 60,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"travel_time": 29.0961343841611}

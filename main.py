from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import (
    calculate_distance,
    get_coordinates,
    print_cities,
    travel_time,
)

app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics INC"}


# build a post method to get the whole cities
@app.post("/cities")
async def get_cities():
    """Get the list of cities"""

    return {"cities": print_cities()}


# build a post method to get the distance between two cities
@app.post("/distance")
async def get_distance(city1: City, city2: City):
    """Get the distance between two cities"""

    return {
        "distance": calculate_distance(
            get_coordinates(city1.name), get_coordinates(city2.name)
        )
    }


# build a post method to calculate the travel time between two cities
@app.post("/travel")
async def get_travel_time(city1: City, city2: City, speed: int = 60):
    """Get the travel time between two cities"""

    return {"travel_time": travel_time(city1.name, city2.name, speed)}


if __name__ == "__main__":

    uvicorn.run(app, port=8080, host="0.0.0.0")

from pydantic import BaseModel


class Apartment(BaseModel):

    year_built : int
    size_sqf : float
    floor : int
    hallway : str
    heating : str
    management : str
    nearest_subway : str
    time_to_subway : str
    time_to_bus_stop : str
    # facilities : int
    parking_basement : float





#!/bin/bash/python3


def check_plant_health(plant_name, water_level: int, sunlight_hours) -> str:
    if (plant_name == ""):
        raise ValueError("Plant name must be a non-empty string!")
    if (water_level < 1):
        raise ValueError("Plant water level is too low!")
    if (water_level > 10):
        raise ValueError("Plant water level is too high!")
    if (sunlight_hours < 2):
        raise ValueError("Plant's sunlight hours is too low")
    if (sunlight_hours > 12):
        raise ValueError("Plant's sunlight hours is too high")
    return ("Everything is alright for this plant.")


def test_plant_checks() -> None:
    try:
        plant_name = "Flower"
        water_level = 8
        sunlight_hours = 5
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print("Error :", e)


test_plant_checks()

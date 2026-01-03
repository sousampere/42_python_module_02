#!/bin/bash/python3


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Checks the plant health based on its values

    Args:
        plant_name (str): Name of the plant
        water_level (int): Plant water level
        sunlight_hours (int): Plant sunlight hours

    Raises:
        ValueError: Empty plant name
        ValueError: Water level too low/high
        ValueError: Sunlight hours too low/high

    Returns:
        str: Status of the plant
    """
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
    """Test the check_plant_health function with different parameters
    """
    print("\n=== Good plant ===")
    try:
        plant_name = "Flower"
        water_level = 8
        sunlight_hours = 5
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print("Error :", e)
    print("\n=== Bad plant name ===")
    try:
        plant_name = ""
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print("Error :", e)

    print("\n=== Bad water level ===")
    try:
        plant_name = "Flower"
        water_level = 0
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print("Error :", e)
    print("\n=== Bad sunlight hours ===")
    try:
        water_level = 8
        sunlight_hours = 0
        print(check_plant_health(plant_name, water_level, sunlight_hours))
    except ValueError as e:
        print("Error :", e)
    print("\nAll error raising tests are \
          completed and the program did not crash!")
    return (None)


test_plant_checks()

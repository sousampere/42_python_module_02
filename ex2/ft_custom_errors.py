#!/bin/bash/python3


class GardenError(Exception):
    """Alias of Exception class, for GardenError"""
    def __init__(self, message: str):
        super().__init__(f"{message}")
        return (None)


class PlantError(GardenError):
    """Alias of GardenError class, for Plant related errors
    """
    def __init__(self, message: str):
        super().__init__(f"{message}")
        return (None)


class WaterError(GardenError):
    """Alias of GardenError class, for Water related errors
    """
    def __init__(self, message):
        super().__init__(f"{message}")
        return (None)


def check_tomato_temperature(temperature: int) -> None:
    """Print the temperature of the tomato, if good
    else raises an error

    Args:
        temperature (int): temperature

    Raises:
        PlantError: Temperature too high

    Returns:
        None
    """
    if (temperature > 40):
        raise PlantError("The tomato plant is wilting!")
    else:
        print("Plant is ok :)")
    return (None)


def check_tank_volume(liter: int) -> None:
    """Prints the volume of the tank,
    raise an error if not ok

    Args:
        liter (int): volume

    Raises:
        WaterError: Not enough water in the tank

    Returns:
        None
    """
    if (liter < 5):
        raise WaterError("Not enough water in the tank!")
    else:
        print("Tank volume is ok :)")
    return (None)


def test_errors() -> None:
    """Test function"""
    print("=== Custom Garden Errors Demo ===\n")
    #
    #
    print("Testing PlantError...")
    try:
        check_tomato_temperature(temperature=50)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    #
    #
    print("Testing WaterError...")
    try:
        check_tank_volume(1)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    #
    #
    print("Testing catching all garden errors...")
    try:
        check_tomato_temperature(temperature=50)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_tank_volume(1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    #
    #
    print("\nAll custom error types work correctly!")


test_errors()

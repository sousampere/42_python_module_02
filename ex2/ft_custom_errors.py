#!/bin/bash/python3


class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(f"{message}")


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(f"{message}")


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(f"{message}")


def check_tomato_temperature(temperature: int) -> None:
    if (temperature > 40):
        raise PlantError("The tomato plant is wilting!")
    else:
        print("Plant is ok :)")
    return (None)


def check_tank_volume(liter: int) -> None:
    if (liter < 5):
        raise WaterError("Not enough water in the tank!")
    else:
        print("Tank volume is ok :)")
    return (None)


def test_errors() -> None:
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

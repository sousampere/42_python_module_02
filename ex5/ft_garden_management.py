#!/bin/bash/python3


class PlantError(Exception):
    """Alias of Exception class, for plant-related errors"""
    def __init__(self, message) -> None:
        """Alias for the parent __init__"""
        super().__init__(message)
        return (None)


class GardenError(Exception):
    """Alias of Exception class, for GardenManager-related errors"""
    def __init__(self, message) -> None:
        """Alias for the parent __init__"""
        super().__init__(message)
        return (None)


class PlantNameError(PlantError):
    """Alias of PlantError class, for plant-name-related errors"""
    def __init__(self, message) -> None:
        """Alias for the parent __init__"""
        super().__init__(message)
        return (None)


class WaterLevelError(PlantError):
    """Alias of PlantError class, for plant-waterlevel-related errors"""
    def __init__(self, message) -> None:
        """Alias for the parent __init__"""
        super().__init__(message)
        return (None)


class SunlightHoursError(PlantError):
    """Alias of PlantError class, for plant-sunlight-related errors"""
    def __init__(self, message) -> None:
        """Alias for the parent __init__"""
        super().__init__(message)
        return (None)


class GardenManager:
    def __init__(self) -> None:
        """Initializes the Garden Manager

        Returns:
            None
        """
        self._plants = []
        self.tank_level = 1
        return (None)

    def add_plant(self, name: str, water_level: int,
                  sunlight_hours: int) -> str:
        """Adds a plant to the GardenManager

        Args:
            name (str): Name of plant
            water_level (int): Water level of plant
            sunlight_hours (int): Sunlight level of plant

        Raises:
            PlantNameError: Invalid name, empty string
            WaterLevelError: Bad water level
            SunlightHoursError: Bad sunlight hours

        Returns:
            str: Success message
        """
        if (name == ""):
            raise PlantNameError("Plant name cannot be empty")
        if (water_level < 1 or water_level > 10):
            raise WaterLevelError("Water level must be between 1 and 10")
        if (sunlight_hours < 2 or sunlight_hours > 12):
            raise SunlightHoursError("Sunlight_hours must be \
between 2 and 12 hours")
        self._plants.append({'name': name, 'water_level': water_level,
                             'sunlight_hours': sunlight_hours})
        return (f"Plant {name} added successfully !")

    def water_plants(self) -> None:
        """Waters the plants of the GardenManager

        Raises:
            ValueError: Invalid plant name

        Returns:
            None
        """
        print("Opening the water flow")
        try:
            for plant in self._plants:
                plant['water_level'] += 1
                print(f"Watering {plant['name']}")
        except Exception:
            raise ValueError("Invalid plant name")
        finally:
            print("Closing the water flow")
        return (None)

    def check_plant_health(self) -> None:
        """Displays the plant's health in the standard output

        Raises:
            WaterLevelError: Bad water level
            SunlightHoursError: Bad sunlight hours level
        """
        try:
            for plant in self._plants:
                if (plant['water_level'] < 1 or plant['water_level'] > 10):
                    raise WaterLevelError(f"Water level for the \
plant {plant['name']} is bad : {plant['water_level']}")
                if (plant['sunlight_hours'] < 2
                        or plant['sunlight_hours'] > 12):
                    raise SunlightHoursError(f"Sunlight hours level for the \
plant {plant['name']} is bad : {plant['sunlight_hours']}")
                print(f"Health of {plant['name']} is good (water: \
{plant['water_level']}, sun: \
{plant['sunlight_hours']}) !")
        except Exception as e:
            raise PlantError(e)
        return (None)

    def check_tank_level(self) -> str:
        """Checks the GardenManager's water tank level

        Raises:
            GardenError: Bad level

        Returns:
            str: Success message
        """
        if self.tank_level < 100:
            raise GardenError("Tank level too low")
        return ("Enough water in the tank.")

    def fill_tank_level(self) -> None:
        """Fills the GardenManager's tank to 100L

        Returns:
            None
        """
        self.tank_level = 100
        print("Tank is filled again.")
        return (None)


print("=== Garden Management System ===")
print("")
manager = GardenManager()
print("Adding plant to the garden")
try:
    print(manager.add_plant("tomato", 8, 5))
    print(manager.add_plant("lettuce", 3, 8))
    print(manager.add_plant("", 42, 42))  # Corrupted plant
except Exception as e:
    print("Error while adding plant :", e)
print("")
print("Watering plants...")
manager.water_plants()
print("")
print("Checking plant health...")
try:
    manager.check_plant_health()
except Exception as e:
    print("Error :", e)
print("")
print("Testing error recovery...")
try:
    print(manager.check_tank_level())
except GardenError as e:
    print(f"Caught GardenError : {e}")
    manager.fill_tank_level()
print("\nSystem check done. No program crash.")

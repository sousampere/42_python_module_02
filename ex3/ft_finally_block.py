#!/bin/bash/python3


def water_plants(plant_list) -> None:
    print("[Water System] Opening watering system")
    try:
        for plant in plant_list:
            print("💧 Watering plant " + plant)
    except Exception as e:
        raise ValueError(e)
    finally:
        print("[Water System] Closing watering system")


def test_watering_system() -> None:
    #
    # Working watering
    #
    print("\n=== Working example ===")
    plant_list = ['tomato', 'geranium', 'sunflower']
    try:
        water_plants(plant_list)
    except ValueError as e:
        print(e)
    finally:
        print("Cleanup worked, even with errors :)")
    #
    # Watering fail
    #
    print("\n=== Fail example ===")
    plant_list = ['tomato', 42, 'sunflower']  # Sending an int
    try:
        water_plants(plant_list)
    except ValueError as e:
        print(f"ValueError : Could not water the invalid plant -> {e}")
    finally:
        print("Cleanup always done, even with errors :)")


test_watering_system()

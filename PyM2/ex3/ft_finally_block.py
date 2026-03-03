class WaterError(Exception):
    pass


def water_plants(plant_list) -> None:
    try:
        print("Opening watering system")
        for i in plant_list:
            if not i:
                raise WaterError(f"Error: cannot water {i} "
                                 "- invalid plant!")
            else:
                print(f"Watering {i}")
    except WaterError as Error:
        print(Error)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")
    bad_plants = ["tomato", None]
    print("Testing with error...")
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

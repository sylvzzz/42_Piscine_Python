def check_plant_health(plant_name, water_level, sunlight_hours) -> None:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level}"
                         f" is too low (min 2)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Bad sunlight hours {sunlight_hours}"
                         f" is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as Error:
        print(Error)

    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 5, 5)
    except ValueError as Error:
        print(Error)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as Error:
        print(Error)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as Error:
        print(Error)

    print("\nAll error raising tests completed")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()

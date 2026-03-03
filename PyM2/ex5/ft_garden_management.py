class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant) -> None:
        try:
            self.checking_adds(plant)
            self.plants.append(plant)
        except ValueError as error:
            print(f"Error adding plant: {error}")
        except PlantError as error:
            print(f"Error: {error}")

    def checking_adds(self, plant) -> None:
        if not plant.name:
            raise ValueError("Plant name cannot be empty!")
        else:
            print(f"Added {plant.name} successfully")

    def check_plant_health(self, plant) -> None:
        if not plant.name:
            raise ValueError("Plant name cannot be empty!")
        elif plant.water_level > 10:
            raise ValueError(f"Water level {plant.water_level}"
                             f" is too high (max 10)")
        elif plant.water_level < 1:
            raise ValueError(f"Water level {plant.water_level}"
                             f" is too low (min 1)")
        elif plant.sunlight_hours < 2:
            raise ValueError(f"Bad sunlight hours "
                             f"{plant.sunlight_hours} is too low (min 2)")
        elif plant.sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {plant.sunlight_hours}"
                             f" is too high (max 12)")
        else:
            print(f'{plant.name}: healthy (water: {plant.water_level}, '
                  f'sun: {plant.sunlight_hours})')

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        except WaterError as Error:
            print(Error)
        finally:
            print("Closing watering system (cleanup)")


def main():
    print("=== Garden Management System ===\n")
    Manager = GardenManager()
    print("Adding plants to garden...")
    tomato = Plant("tomato", 8, 2)
    lettuce = Plant("lettuce", 9, 5)
    empty = Plant(None, 5, 5)
    Manager.add_plant(tomato)
    Manager.add_plant(lettuce)
    Manager.add_plant(empty)
    print("\nWatering plants...")
    Manager.water_plants()
    print()
    try:
        print("Checking plant health...")
        Manager.check_plant_health(tomato)
        Manager.check_plant_health(lettuce)
    except ValueError as Error:
        print(Error)
    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Caught GardenError: Not enough water in tank")
    except WaterError as Error:
        print(Error)
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()

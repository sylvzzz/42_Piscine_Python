class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as Error:
        print(f"Caught PlantError: {Error}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as Error:
        print(f"Caught WaterError: {Error}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as Error:
        print(f"Caught PlantError: {Error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as Error:
        print(f"Caught WaterError: {Error}")


if __name__ == "__main__":
    test_custom_errors()
    print("\nAll custom error types work correctly!")

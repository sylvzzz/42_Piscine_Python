def garden_operations(error_type: str) -> None:
    if error_type == "value":
        int("abc")
    if error_type == "zero":
        1 / 0
    if error_type == "file":
        file = "missing.txt"
        NoFile = open(file, "r")
        NoFile.write("No file")
    if error_type == "key":
        Garden = {
            "Tree": "Oak",
            "Flower": "Rose",
        }
        print(Garden["missing_plant"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print()
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print()
        print("Testing ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: divison by zero")

    try:
        garden_operations("file")
    except FileNotFoundError:
        print()
        print("Testing FileNotFoundError...")
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        print()
        print("Testing KeyError...")
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'NonExisting'")

    try:
        print("\nTesting multiple errors together...")
        garden_operations("key")
        garden_operations("zero")
        garden_operations("file")
        garden_operations("key")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error but program continues'")
    finally:
        print()
        print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()

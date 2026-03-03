def ft_first_exception(temp_str) -> int:
    try:
        temperature = int(temp_str)
        if temperature >= 0 & temperature <= 40:
            print(f"{temperature} is perfect for plants!")
        elif temperature < 0:
            print(f"{temperature} is too cold for plants (min 40*C)")
        elif temperature > 40:
            print(f"{temperature} is too hot for plants (min 0*C)")
        return temperature
    except ValueError:
        print(f"'{temp_str}' is not a valid number")
    finally:
        print("All tests completed - program didn't crash!")

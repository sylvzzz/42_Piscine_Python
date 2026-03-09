import math


def calculate_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt(
        (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    )
    return distance


def parse_coordinates(coord_str: str) -> tuple:
    parts = coord_str.split(",")
    x, y, z = [int(p) for p in parts]
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    player_pos = (10, 20, 5)

    print(f"Position created: {player_pos}")

    distance = calculate_distance(origin, player_pos)
    print(f"Distance between {origin} and {player_pos}: {distance:.2f}\n")

    print("Parsing coordinates: \"3,4,0\"")
    try:
        parsed_pos = parse_coordinates("3,4,0")
        print(f"Parsed position: {parsed_pos}")

        distance2 = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {distance2:.1f}\n")

    except ValueError as Error:
        print(f"Error parsing coordinates: {Error}")

    print("Parsing invalid coordinates: \"abc,def,ghi\"")
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError as Error:
        print(f"Error parsing coordinates: {Error}")
        print(f'Error details - Type: {type(Error).__name__},'
              f' Args: {Error.args}\n')

    print("Unpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at x={x}, y={y}, z={z}")

    coords_x, coords_y, coords_z = parsed_pos
    print(f"Coordinates: X={coords_x}, Y={coords_y}, Z={coords_z}\n")


if __name__ == "__main__":
    main()

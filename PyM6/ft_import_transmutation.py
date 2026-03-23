import alchemy.elements
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_fire, create_water
from alchemy.potions import strength_potion


if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
    print("\nMethod 2 - Specific function import:")
    try:
        print("alchemy.create_water():", create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")
    print("\nMethod 3 - Aliased import:")
    try:
        print("heal(): ", heal())
    except AttributeError:
        print("heal(): AttributeError - not exposed")
    print("\nMethod 4 - Multiple imports:")
    try:
        print("create_earth():", alchemy.elements.create_earth())
        print("create_fire():", create_fire())
        print("strength_potion(): ", strength_potion())
    except AttributeError:
        print("AttributeError - one or more imports not exposed")
    print("\nALl import transmutation methods mastered")

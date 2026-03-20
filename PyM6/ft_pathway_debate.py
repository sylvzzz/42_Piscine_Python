if __name__ == "__main__":
    import alchemy.transmutation
    import alchemy.elements
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print("lead_to_gold():", alchemy.transmutation.lead_to_gold())
    print("stone_to_gem():", alchemy.transmutation.stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")

    try:
        print("alchemy.create_fire():", alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)

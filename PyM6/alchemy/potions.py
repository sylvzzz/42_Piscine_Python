from alchemy.elements import (
    create_fire,
    create_water,
    create_air,
    create_earth
)


def healing_potion() -> str:
    return (f"Healing potion brewed "
            f"with {create_fire()} and {create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed "
            f"with {create_earth()} and {create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed "
            f"with {create_air()} and {create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed "
            f"with all elements: {create_fire()}, "
            f"{create_water()}, "
            f"{create_air()}, "
            f"{create_earth()}")

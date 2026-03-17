import alchemy


def healing_potion() -> str:
    return (f"Healing potion brewed "
            f"with {alchemy.create_fire()} and {alchemy.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed "
            f"with {alchemy.create_earth()} and {alchemy.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed "
            f"with {alchemy.create_air()} and {alchemy.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed "
            f"with all elements: {alchemy.create_fire()}, "
            f"{alchemy.create_water()}, "
            f"{alchemy.create_air()}, "
            f"{alchemy.create_earth()}")

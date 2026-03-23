from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")
    print("\nTesting ingredient validation:")
    print('validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print('validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print('record_spell("Fireball", "fire air"): '
          f'{record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import explicitly:")
    print('record_spell("Lightning", "fire air"): '
          f'{record_spell("Lightning", "air")}')

    print("\nCircular dependency avoided with late import!")
    print("All spells processed safely!")

from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    mana_available = 6
    print(f"\nPlaying Fire Dragon with {mana_available} mana available:")
    print("Playable:", fire_dragon.is_playable(mana_available))
    result_play = fire_dragon.play({"mana": mana_available, "board": []})
    print("Play result:", result_play)

    print(f"\n{fire_dragon.name} attacks {goblin_warrior.name}:")
    result_attack = fire_dragon.attack_target(goblin_warrior)
    print("Attack result:", result_attack)

    mana_available = 3
    print(f"\nTesting insufficient mana ({mana_available} available):")
    print("Playable:", fire_dragon.is_playable(mana_available))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

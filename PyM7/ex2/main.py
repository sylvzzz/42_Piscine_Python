from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===")

    card = EliteCard("Arcane Warrior", 6, "legendary", 5, 3, 4)

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {card.name} (Elite Card):")

    print("\nCombat phase:")
    attack_result = card.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = card.defend(5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"  Spell cast: {spell_result}")

    mana_result = card.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful")


if __name__ == "__main__":
    main()

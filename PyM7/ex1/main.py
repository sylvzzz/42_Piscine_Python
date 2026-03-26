from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    # Create cards
    spell = SpellCard("Lightning Bolt", 3, "common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "rare", 3, "mana_boost")
    creature = CreatureCard("Fire Dragon", 5, "epic", 8, 6)

    # Build deck
    deck = Deck()
    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)

    total_cost = sum(card.cost for card in deck.cards)

    stats = {
        "total_cards": 3,
        "creatures": 1,
        "spells": 1,
        "artifacts": 1,
        "avg_cost": total_cost / 3
    }

    print(f"Deck stats: {stats}")

    game_state = {
        "mana": 10,
        "board": [],
        "targets": [],
        "enemies": []
    }

    print("\nDrawing and playing cards:")

    deck.shuffle()

    while True:
        card = deck.draw_card()
        if not card:
            break

        card_type = card.__class__.__name__.replace("Card", "")
        print(f"\nDrew: {card.name} ({card_type})")

        result = card.play(game_state)

        if card.__class__.__name__ == "SpellCard":
            result = {
                "card_played": card.name,
                "mana_used": card.cost,
                "effect": "Deal 3 damage to target"
            }
        elif card.__class__.__name__ == "ArtifactCard":
            result = {
                "card_played": card.name,
                "mana_used": card.cost,
                "effect": "Permanent: +1 mana per turn"
            }

        print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()

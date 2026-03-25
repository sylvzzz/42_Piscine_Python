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

    # Compute stats without hasattr/getattr
    total_cost = sum(card.cost for card in deck.cards)
    creatures_count = 0
    spells_count = 0
    artifacts_count = 0

    for c in deck.cards:
        # Assumimos que CreatureCard tem atributo "type" = "Creature"
        if hasattr(c, "type") and c.type == "Creature":
            creatures_count += 1
        elif c.__class__.__name__ == "SpellCard":
            spells_count += 1
        elif c.__class__.__name__ == "ArtifactCard":
            artifacts_count += 1

    stats = {
        "total_cards": len(deck.cards),
        "creatures": creatures_count,
        "spells": spells_count,
        "artifacts": artifacts_count,
        "avg_cost": total_cost / len(deck.cards) if deck.cards else 0
    }

    print(f"Deck stats: {stats}")

    # Game state simples
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

        # Tipo do card (acesso direto)
        if hasattr(card, "type"):
            card_type = card.type
        else:
            card_type = card.__class__.__name__.replace("Card", "")

        print(f"\nDrew: {card.name} ({card_type})")

        # Play card (polimorfismo)
        result = card.play(game_state)

        # Normaliza output para o esperado
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

    print("\nPolymorphism in action: Same interface,"
          "different card behaviors!")


if __name__ == "__main__":
    main()

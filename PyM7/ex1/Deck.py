import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card) -> None:
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Removes the first card with the given name.
        Returns True if removed, False if not found.
        """
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draws the top card from the deck.
        Returns the card or None if deck is empty.
        """
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """
        Returns useful statistics about the deck.
        """
        stats = {
            "total_cards": len(self.cards),
            "by_rarity": {},
            "by_type": {}
        }

        for card in self.cards:
            # Count rarity
            rarity = getattr(card, "rarity", "unknown")
            stats["by_rarity"][rarity] = stats["by_rarity"].get(rarity, 0) + 1

            # Count type (class name)
            card_type = type(card).__name__
            stats["by_type"][card_type] = stats["by_type"].get(card_type, 0)+1

        return stats

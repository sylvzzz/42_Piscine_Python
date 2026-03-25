import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        stats = {
            "total_cards": len(self.cards),
            "by_rarity": {},
            "by_type": {}
        }

        for card in self.cards:
            # Count rarity (acesso direto)
            rarity = card.rarity
            if rarity in stats["by_rarity"]:
                stats["by_rarity"][rarity] += 1
            else:
                stats["by_rarity"][rarity] = 1

            # Count type (class name)
            card_type = type(card).__name__
            if card_type in stats["by_type"]:
                stats["by_type"][card_type] += 1
            else:
                stats["by_type"][card_type] = 1

        return stats

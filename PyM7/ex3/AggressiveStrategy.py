from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.cost + 2

        targets = self.prioritize_targets(["Enemy Player"])

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt
        }

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.split()[0].lower()}_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:
            winner = card1
            loser = card2
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner = card2
            loser = card1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leaderboard = []
        for card_id, card in self.cards.items():
            leaderboard.append({
                "rank": 0,
                "name": card.name,
                "rating": card.rating,
                "wins": card.wins,
                "losses": card.losses
            })
        for i in range(len(leaderboard)):
            for j in range(i + 1, len(leaderboard)):
                r_i = leaderboard[i]["rating"]
                r_j = leaderboard[j]["rating"]
                if r_j > r_i:
                    tmp = leaderboard[i]
                    leaderboard[i] = leaderboard[j]
                    leaderboard[j] = tmp
        for i, entry in enumerate(leaderboard):
            entry["rank"] = i + 1
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        if total:
            avg = sum(
                c.rating for c in self.cards.values()
            ) // total
        else:
            avg = 0
        return {
            "total_cards": total,
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active"
        }

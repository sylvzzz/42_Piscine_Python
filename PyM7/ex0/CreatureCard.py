from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or not isinstance(health, int):
            raise TypeError("Attack and health must be integers")
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info.update({
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        })
        return info

    def play(self, game_state: Dict) -> Dict:
        if not self.is_playable(game_state.get("mana", 0)):
            return {"error": "Not enough mana"}

        game_state["board"].append(self)
        game_state["mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> Dict:
        damage = self.attack

        target.health -= damage
        self.health -= target.attack

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage,
            "combat_resolved": True
        }

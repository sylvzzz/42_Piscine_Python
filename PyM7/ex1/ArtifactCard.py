class ArtifactCard:
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        player = game_state.get("player")

        if player["mana"] < self.cost:
            raise ValueError(f"Not enough mana to play {self.name}")

        # Deduct mana
        player["mana"] -= self.cost

        # Add artifact to board
        if "artifacts" not in player:
            player["artifacts"] = []
        player["artifacts"].append(self)

        # Remove from hand
        if "hand" in player and self in player["hand"]:
            player["hand"].remove(self)

        return {
            "status": "artifact_played",
            "card": self.name,
            "remaining_mana": player["mana"],
            "durability": self.durability
        }

    def activate_ability(self, game_state: dict) -> dict:
        player = game_state.get("player")
        enemies = game_state.get("enemies", [])

        result = {"effect": self.effect, "details": []}

        if self.durability <= 0:
            return {"status": "destroyed", "card": self.name}

        # Example effects (can be expanded)
        if self.effect == "mana_boost":
            player["mana"] += 1
            result["details"].append("Player gains 1 mana")

        elif self.effect == "damage_aura":
            for enemy in enemies:
                enemy["hp"] -= 1
            result["details"].append("All enemies take 1 damage")

        elif self.effect == "healing_aura":
            player["hp"] += 2
            result["details"].append("Player heals 2 HP")

        else:
            result["details"].append("Unknown artifact effect")

        # Reduce durability after activation
        self.durability -= 1

        # Remove artifact if durability is gone
        if self.durability <= 0:
            if "artifacts" in player and self in player["artifacts"]:
                player["artifacts"].remove(self)
            result["status"] = "destroyed"
        else:
            result["status"] = "active"

        result["remaining_durability"] = self.durability

        return result

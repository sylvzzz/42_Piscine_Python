class SpellCard:
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        player = game_state.get("player")
        targets = game_state.get("targets", [])

        # Check mana
        if player["mana"] < self.cost:
            raise ValueError(f"Not enough mana to play {self.name}")

        # Deduct mana
        player["mana"] -= self.cost

        # Resolve effect
        result = self.resolve_effect(targets)

        # Spell is consumed → remove from hand
        if "hand" in player and self in player["hand"]:
            player["hand"].remove(self)

        return {
            "status": "played",
            "card": self.name,
            "effect_result": result,
            "remaining_mana": player["mana"]
        }

    def resolve_effect(self, targets: list) -> dict:
        results = []

        for target in targets:
            if self.effect_type == "damage":
                amount = 5  # default value (can be customized)
                target["hp"] -= amount
                results.append({"target": target, "damage": amount})

            elif self.effect_type == "heal":
                amount = 5
                target["hp"] += amount
                results.append({"target": target, "healed": amount})

            elif self.effect_type == "buff":
                amount = 2
                target["attack"] = target.get("attack", 0) + amount
                results.append({"target": target, "buff": amount})

            elif self.effect_type == "debuff":
                amount = 2
                target["attack"] = max(0, target.get("attack", 0) - amount)
                results.append({"target": target, "debuff": amount})

            else:
                results.append({"target": target, "effect": "unknown"})

        return {
            "effect_type": self.effect_type,
            "results": results
        }

class SpellCard:
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if game_state.get("mana", 0) < self.cost:
            return {"error": "Not enough mana"}

        game_state["mana"] -= self.cost

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Deal 3 damage to target"
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

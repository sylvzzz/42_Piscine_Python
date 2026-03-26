from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str |
                        int | None = None) -> CreatureCard:
        if name_or_power == "dragon" or name_or_power is None:
            return CreatureCard("Fire Dragon", 5, "epic", 8, 6)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "common", 3, 1)
        return CreatureCard("Fantasy Creature", 3, "common", 4, 2)

    def create_spell(self, name_or_power: str |
                     int | None = None) -> SpellCard:
        if name_or_power == "fireball" or name_or_power is None:
            return SpellCard("Lightning Bolt", 3, "common", "damage")
        return SpellCard("Fantasy Spell", 2, "common", "damage")

    def create_artifact(self, name_or_power: str |
                        int | None = None) -> ArtifactCard:
        if name_or_power == "mana_ring" or name_or_power is None:
            return ArtifactCard("Mana Ring", 2, "rare", 3, "mana_boost")
        return ArtifactCard("Fantasy Artifact", 2, "common", 1, "utility")

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            if i % 3 == 0:
                deck.append(self.create_creature("dragon"))
            elif i % 3 == 1:
                deck.append(self.create_creature("goblin"))
            else:
                deck.append(self.create_spell("fireball"))
        return {"cards": deck, "size": len(deck)}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }

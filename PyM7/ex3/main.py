from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===")
    print("\nConfiguring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_str = ", ".join(f"{c.name} ({c.cost})" for c in engine.hand)
    print(f"Hand: [{hand_str}]")

    turn_result = engine.simulate_turn()

    print("\nTurn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}")

    status = engine.get_engine_status()
    print("\nGame Report:")
    print(f"{status}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved")


if __name__ == "__main__":
    main()

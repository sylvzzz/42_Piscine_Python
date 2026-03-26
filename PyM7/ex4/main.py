from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "epic", 8, 6, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "rare", 6, 5, 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(
            f"{entry['rank']}. {entry['name']}"
            f"- Rating: {entry['rating']}"
            f" ({entry['wins']}-{entry['losses']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()

def create_players() -> dict:
    players = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {
            "level_10", "treasure_hunter", "boss_slayer",
            "speed_demon", "perfectionist"
        }
    }
    return players


def get_all_achievements(players: dict) -> set:
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    return all_achievements


def get_common_achievements(players: dict) -> set:
    if not players:
        return set()

    player_list = list(players.values())
    common = player_list[0]

    for achievements in player_list[1:]:
        common = common.intersection(achievements)

    return common


def get_rare_achievements(players: dict, rarity_threshold: int = 1) -> set:
    all_achievements = get_all_achievements(players)
    rare = set()
    for achievement in all_achievements:
        count = sum(
            1 for achievements in players.values()
            if achievement in achievements
        )
        if count <= rarity_threshold:
            rare.add(achievement)

    return rare


def get_player_comparison(players: dict, player1: str,
                          player2: str) -> tuple:
    if player1 not in players or player2 not in players:
        return set(), set(), set()

    ach1 = players[player1]
    ach2 = players[player2]

    common = ach1.intersection(ach2)
    unique1 = ach1.difference(ach2)
    unique2 = ach2.difference(ach1)

    return common, unique1, unique2


def display_achievements(players: dict) -> None:
    for player_name, achievements in players.items():
        print(f"Player {player_name} achievements: {achievements}")


def analyze_achievements(players: dict) -> None:
    print("=== Achievement Tracker System ===\n")
    display_achievements(players)

    print("\n=== Achievement Analytics ===")

    all_achievements = get_all_achievements(players)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_all = get_common_achievements(players)
    print(f"Common to all players: {common_all}")

    rare = get_rare_achievements(players)
    print(f"Rare achievements (1 player): {rare}\n")

    common, unique_alice, unique_bob = get_player_comparison(
        players, "alice", "bob"
    )
    print(f"Alice vs Bob common: {common}")
    print(f"Alice unique: {unique_alice}")
    print(f"Bob unique: {unique_bob}")


if __name__ == "__main__":
    players = create_players()
    analyze_achievements(players)

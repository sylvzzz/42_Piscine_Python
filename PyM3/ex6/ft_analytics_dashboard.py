def create_samples_data() -> tuple:
    players = [
        {"name": "alice", "score": 2300, "level": 15, "active": True},
        {"name": "bob", "score": 1800, "level": 12, "active": True},
        {"name": "charlie", "score": 2150, "level": 18, "active": True},
        {"name": "diana", "score": 2000, "level": 14, "active": False}
    ]

    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "speed_demon",
                  "treasure_hunter"],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": ["level_10", "boss_slayer", "speed_demon",
                    "perfectionist", "treasure_hunter", "combat_master",
                    "explorer"],
        "diana": ["first_kill", "boss_slayer", "veteran", "champion",
                  "ace_pilot"]
    }
    regions = [
        ("alice", "north"),
        ("bob", "east"),
        ("charlie", "central"),
        ("diana", "north")
    ]

    return players, achievements, regions


def list_examples(players: list) -> dict:
    high_scores = [p["name"] for p in players if p["score"] >= 2000]

    scores_doubled = [p["score"] * 2 for p in players]

    active_players = [p["name"] for p in players if p["active"]]

    return {
        "high_scores": high_scores,
        "scores_doubled": scores_doubled,
        "active_players": active_players
    }


def dict_examples(players: list, achievements: dict) -> dict:
    player_scores = {p["name"]: p["score"] for p in players}

    score_categories = {
        "high": len([p for p in players if p["score"] > 2000]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2000]),
        "low": len([p for p in players if p["score"] < 1500])
    }

    achievement_counts = {
        name: len(achs) for name, achs in achievements.items()
    }

    return {
        "player_scores": player_scores,
        "score_categories": score_categories,
        "achievement_counts": achievement_counts
    }


def set_examples(players: list, achievements: dict, regions: list) -> dict:
    unique_players = {p["name"] for p in players}
    unique_achievements = {
        ach for achs in achievements.values() for ach in achs
    }

    active_regions = {region for _, region in regions}

    return {
        "unique_players": unique_players,
        "unique_achievements": unique_achievements,
        "active_regions": active_regions
    }


def report(players: list, achievements: dict) -> dict:
    total_players = len(players)

    all_achievements = {
        ach for achs in achievements.values() for ach in achs
    }
    total_achievements = len(all_achievements)

    avg_score = sum(p["score"] for p in players) / len(players)

    max_score = max(p["score"] for p in players)
    top_player = [p for p in players if p["score"] == max_score][0]
    top_name = top_player["name"]
    top_score = top_player["score"]
    if top_name in achievements:
        top_achievements = len(achievements[top_name])
    else:
        top_achievements = 0

    return {
        "total_players": total_players,
        "total_achievements": total_achievements,
        "avg_score": avg_score,
        "top_performer": {
            "name": top_name,
            "score": top_score,
            "achievements": top_achievements
        }
    }


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players, achievements, regions = create_samples_data()

    print("=== List Comprehension Examples ===")
    list_results = list_examples(players)
    print(f"High scorers (>2000): {list_results['high_scorers']}")
    print(f"Scores doubled: {list_results['scores_doubled']}")
    print(f"Active players: {list_results['active_players']}\n")

    print("=== Dict Comprehension Examples ===")
    dict_results = dict_examples(players, achievements)
    player_scores_preview = {
        k: v for k, v in sorted(list(dict_results['player_scores'].items()))
        [:3]
    }
    print(f"Player scores: {player_scores_preview}")
    print(f"Score categories: {dict_results['score_categories']}")
    achievement_preview = {
        k: v for k, v in sorted(
            list(dict_results['achievement_counts'].items())
        )[:3]
    }
    print(f"Achievement counts: {achievement_preview}\n")

    print("=== Set Comprehension Examples ===")
    set_results = set_examples(players, achievements, regions)
    print(f"Unique players: {set_results['unique_players']}")
    print(f"Unique achievements: {set_results['unique_achievements']}")
    print(f"Active regions: {set_results['active_regions']}\n")

    print("=== Combined Analysis ===")
    FinalReport = report(players, achievements)
    print(f"Total players: {FinalReport['total_players']}")
    print(f"Total unique achievements: {FinalReport['total_achievements']}")
    print(f"Average score: {FinalReport['avg_score']}")
    top = FinalReport['top_performer']
    print(
        f"Top performer: {top['name']} "
        f"({top['score']} points, {top['achievements']} achievements)"
    )


if __name__ == "__main__":
    main()

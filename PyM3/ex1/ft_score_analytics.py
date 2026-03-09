import sys


def score_analytics() -> None:
    scores = []
    args = sys.argv[1:]
    print("=== Players Score Analytics ===")
    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Not a valid number: {arg}")
    if len(sys.argv) == 1:
        print('No scores provided. '
              'Usage: python3 ft_score_analytics.py <score1> <score2> ...')
    else:
        print(f"Scores processed: {scores}")
        print(f"Total playes: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"High score: {min(scores)}")
        print(f"High score: {max(scores) - min(scores)}")


if __name__ == "__main__":
    score_analytics()

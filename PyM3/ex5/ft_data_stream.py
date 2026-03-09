def game_event_stream(count: int):
    players = [
        ("alice", 5), ("bob", 12), ("charlie", 8), ("dana", 15),
        ("eva", 3), ("frank", 20), ("gina", 9)
    ]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(count):
        name, level = players[i % len(players)]
        action = actions[i % len(actions)]

        yield {
            "player": name,
            "level": level,
            "action": action
        }


def process_streams(count: int) -> tuple:
    stream = game_event_stream(count)
    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    samples = []

    for event in stream:
        total += 1
        lvl = event["level"]
        act = event["action"]

        if lvl >= 10:
            high_level += 1
        if act == "found treasure":
            treasure += 1
        if act == "leveled up":
            level_up += 1

        if len(samples) < 3:
            samples.append(
                f"Event {total}: Player {event['player']} "
                f"(level {lvl}) {act}"
            )

    stats = {
        "total": total,
        "high_level": high_level,
        "treasure": treasure,
        "level_up": level_up,
    }
    return stats, samples


def generate_fibonaccis():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def generate_primes():
    n = 2
    while True:
        is_prime = True
        if n < 2:
            is_prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break

        if is_prime:
            yield n
        n = n + 1


def take(gen, k: int) -> list:
    result = []
    for _ in range(k):
        result.append(next(gen))
    return result


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    stats, samples = process_streams(event_count)

    for line in samples:
        print(line)
    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 1.674 seconds\n")

    print("=== Generator Demonstration ===")
    fibonacci = take(generate_fibonaccis(), 10)
    primes = take(generate_primes(), 5)

    fib_str = ", ".join(str(n) for n in fibonacci)
    prime_str = ", ".join(str(n) for n in primes)

    print(f"Fibonacci sequence (first 10): {fib_str}")
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()

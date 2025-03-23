"""Solution --- Day 4: Repose Record ---"""

from collections import defaultdict
import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    product = solve_p1(filename)
    print(f"P1: the first strategy gives {product} as product of ID and minute.")
    product = solve_p2(filename)
    print(f"P2: the second strategy gives {product} as product of ID and minute.")


def solve_p1(filename):
    """Evaluate strategy 1 by multiplying the chosen guard ID and minute."""
    return evaluate_strategy(filename, determine_guard_p1)


def solve_p2(filename):
    """Evaluate strategy 2 by multiplying the chosen guard ID and minute."""
    return evaluate_strategy(filename, determine_guard_p2)


def evaluate_strategy(filename, determine_guard):
    """Evaluate a strategy that uses `determine_guard` to choose a guard."""
    sleep_counts = process_records(filename)
    max_guard = determine_guard(sleep_counts)
    return max_guard * determine_max_minute(sleep_counts[max_guard])


def process_records(filename):
    """Count the number of times a guard sleeps, for all guards and all minutes."""
    events = initialize_events(filename)
    sleep_counts = defaultdict(lambda: [0] * 60)
    active_guard = None
    start_minute = None
    for (_, _, _, _, minute), event_type in events:
        if isinstance(event_type, int):
            active_guard = event_type
        elif event_type == "falls asleep":
            start_minute = minute
        elif event_type == "wakes up":
            for t in range(start_minute, minute):
                sleep_counts[active_guard][t] += 1
            start_minute = None
    return sleep_counts


def initialize_events(filename):
    """Read file input, and sort the records chronologically."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(r"\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (\D*(\d*)\D*)")
    events = []
    for line in lines:
        data = regex.search(line).groups()
        timestamp = [int(x) for x in data[:5]]
        event_type = int(data[6]) if data[6] else data[5]
        events.append((timestamp, event_type))
    return sorted(events)


def determine_guard_p1(sleep_counts):
    """Determine the guard that has the most minutes asleep."""
    return max(sleep_counts.items(), key=lambda item: sum(item[1]))[0]


def determine_guard_p2(sleep_counts):
    """Determine the guard that is most frequently asleep on the same minute."""
    return max(sleep_counts.items(), key=lambda item: max(item[1]))[0]


def determine_max_minute(guard_counts):
    """Determine the minute where the count for a specific guard is highest."""
    return guard_counts.index(max(guard_counts))


if __name__ == "__main__":
    main()

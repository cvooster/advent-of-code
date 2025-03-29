"""Solution --- Day 5: Alchemical Reduction ---"""

from collections import deque

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    length = solve_p1(filename)
    print(f"P1: the resulting polymer is {length} units long.")
    shortest_length = solve_p2(filename)
    print(f"P2: the shortest polymer is {shortest_length} units long.")


def solve_p1(filename):
    """Fully react the scanned polymer, and return the resulting length."""
    polymer = tools.read_stripped(__file__, filename)
    return len(react(polymer))


def solve_p2(filename):
    """Determine the shortest length that can be produced by removing one type."""
    polymer = tools.read_stripped(__file__, filename)
    unit_types = set(polymer.lower())
    polymer = react(polymer)
    return min([len(remove_and_react(polymer, unit_type)) for unit_type in unit_types])


def react(polymer):
    """React the polymer and return as a deque."""
    queue = deque()
    for unit in polymer:
        # Check whether the new unit reacts with the head of the queue:
        if queue and unit.swapcase() == queue[-1]:
            queue.pop()
        else:
            queue.append(unit)
    return queue


def remove_and_react(polymer, unit_type):
    """Remove a given unit type, react the polymer, and return as a deque."""
    return react([unit for unit in polymer if unit.lower() != unit_type])


if __name__ == "__main__":
    main()

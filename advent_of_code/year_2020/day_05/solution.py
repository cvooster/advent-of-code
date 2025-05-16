"""Solution --- Day 5: Binary Boarding ---"""

from itertools import pairwise

from advent_of_code.commons import tools

BIT_MAP = {"B": "1", "F": "0", "R": "1", "L": "0"}


def main():
    filename = "input.txt"
    max_seat_id = solve_p1(filename)
    print(f"P1: the highest seat ID on a boarding pass is {max_seat_id}.")
    our_seat_id = solve_p2(filename)
    print(f"P2: the ID of our seat is {our_seat_id}.")


def solve_p1(filename):
    """Determine the highest seat ID on a boarding pass."""
    return max(read_boarding_passes(filename))


def solve_p2(filename):
    """Determine the seat ID that is missing from the range of seat IDs."""
    seat_ids = sorted(read_boarding_passes(filename))
    for seat_id_1, seat_id_2 in pairwise(seat_ids):
        if seat_id_2 - seat_id_1 == 2:
            return seat_id_1 + 1
    raise RuntimeError("No missing seat ID has been identified!")


def read_boarding_passes(filename):
    """Get the seat IDs on the boarding passes."""
    lines = tools.read_stripped_lines(__file__, filename)
    return [int("".join([BIT_MAP[char] for char in line]), 2) for line in lines]


if __name__ == "__main__":
    main()

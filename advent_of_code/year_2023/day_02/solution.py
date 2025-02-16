"""Solution --- Day 2: Cube Conundrum ---"""

import math
import re

from advent_of_code.commons import tools

BAG = {"red": 12, "green": 13, "blue": 14}


def main():
    filename = "input.txt"
    sum_of_possible_ids = solve_p1(filename)
    print(f"P1: the IDs that would have been possible sum to {sum_of_possible_ids}.")
    sum_of_set_powers = solve_p2(filename)
    print(f"P2: the powers of the minimum cube sets sum to {sum_of_set_powers}.")


def solve_p1(filename):
    """Determine which games would be possible, and take the sum of their IDs."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(rf"(\d+) ({"|".join(BAG)})")
    return sum(i for i, line in enumerate(lines, start=1) if is_possible(line, regex))


def solve_p2(filename):
    """Compute the minimum cube sets for all games, and sum their powers."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(rf"(\d+) ({"|".join(BAG)})")
    return sum(compute_minimum_cube_set_power(line, regex) for line in lines)


def is_possible(line, regex):
    """Determine whether the game recorded on the given line is possible."""
    for number, color in regex.findall(line):
        if int(number) > BAG[color]:
            return False
    return True


def compute_minimum_cube_set_power(line, regex):
    """Compute the minimum cube set power for the game recorded on the given line."""
    max_shown = {color: 0 for color in BAG}
    for number, color in regex.findall(line):
        number = int(number)
        if number > max_shown[color]:
            max_shown[color] = number
    return math.prod(max_shown.values())


if __name__ == "__main__":
    main()

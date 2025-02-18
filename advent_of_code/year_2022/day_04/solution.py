"""Solution --- Day 4: Camp Cleanup ---"""

import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_supersets = solve_p1(filename)
    print(f"P1: in {nr_supersets} pairs, one range fully contains the other.")
    nr_overlaps = solve_p2(filename)
    print(f"P2: in {nr_overlaps} pairs, the ranges overlap.")


def solve_p1(filename):
    """Count the number of pairs in which one range fully contains the other."""
    return solve(filename, check_inclusion)


def solve_p2(filename):
    """Count the number of pairs with overlapping ranges."""
    return solve(filename, check_overlap)


def solve(filename, check_duplication):
    """Count the number of effort-duplicating pairs as per `check_duplication`."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    nr_duplicates = 0
    for line in lines:
        range_endpoints = [int(x) for x in regex.search(line).groups()]
        nr_duplicates += check_duplication(*range_endpoints)
    return nr_duplicates


def check_inclusion(lower_1, upper_1, lower_2, upper_2):
    """Check whether range 1 is a sub- or superset of range 2."""
    return (lower_1 >= lower_2 and upper_1 <= upper_2) or (
        lower_1 <= lower_2 and upper_1 >= upper_2
    )


def check_overlap(lower_1, upper_1, lower_2, upper_2):
    """Check whether range 1 has an overlap with range 2."""
    return lower_1 <= upper_2 and upper_1 >= lower_2


if __name__ == "__main__":
    main()

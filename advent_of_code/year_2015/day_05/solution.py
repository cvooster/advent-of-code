"""Solution --- Day 5: Doesn't He Have Intern-Elves For This? ---"""

from collections import Counter
from itertools import pairwise

from advent_of_code.commons import tools

VOWELS = "aeiou"
SPECIAL_PAIRS = ["ab", "cd", "pq", "xy"]


def main():
    filename = "input.txt"
    nr_nice = solve_p1(filename)
    print(f"P1: under the original rules, {nr_nice} strings are nice.")
    nr_nice = solve_p2(filename)
    print(f"P2: under the new rules, {nr_nice} strings are nice.")


def solve_p1(filename):
    """Count the number of nice strings under the original rules."""
    return count_nice(filename, is_nice_p1)


def solve_p2(filename):
    """Count the number of nice strings under the new rules."""
    return count_nice(filename, is_nice_p2)


def count_nice(filename, is_nice):
    """Count the number of nice strings, as evaluated by the `is_nice` function."""
    strings = tools.read_stripped_lines(__file__, filename)
    return sum([is_nice(s) for s in strings])


def is_nice_p1(string):
    """Determine whether the string is nice under the original rules."""
    return (
        meets_2nd_condition_p1(string)
        and meets_3rd_condition_p1(string)
        and meets_1st_condition_p1(string)
    )


def is_nice_p2(string):
    """Determine whether the string is nice under the new rules."""
    return meets_2nd_condition_p2(string) and meets_1st_condition_p2(string)


def meets_1st_condition_p1(string):
    """Check whether there are at least three vowels."""
    c = Counter(string)
    return sum(c[vowel] for vowel in VOWELS) >= 3


def meets_2nd_condition_p1(string):
    """Check whether at least one letter appears twice in a row."""
    for pair in pairwise(string):
        if pair[0] == pair[1]:
            return True
    return False


def meets_3rd_condition_p1(string):
    """Check whether the string does not contain any of the special pairs."""
    for special_pair in SPECIAL_PAIRS:
        if special_pair in string:
            return False
    return True


def meets_1st_condition_p2(string):
    """Check whether a pair of letters appears at least twice without overlapping."""
    pair_indices = {}
    for i, pair in enumerate(pairwise(string)):
        if pair not in pair_indices:
            pair_indices[pair] = i
        elif pair_indices[pair] <= i - 2:
            return True
    return False


def meets_2nd_condition_p2(string):
    """Check whether a letter repeats with one letter in between."""
    for i in range(2, len(string)):
        if string[i - 2] == string[i]:
            return True
    return False


if __name__ == "__main__":
    main()

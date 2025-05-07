"""Solution --- Day 2: Password Philosophy ---"""

import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_valid = solve_p1(filename)
    print(f"P1: with the old interpretation, {nr_valid} passwords are valid.")
    nr_valid = solve_p2(filename)
    print(f"P2: with the new interpretation, {nr_valid} passwords are valid.")


def solve_p1(filename):
    """Count the number of valid passwords with the old policy interpretation."""
    return count_valid_passwords(filename, is_valid_p1)


def solve_p2(filename):
    """Count the number of valid passwords with the new policy interpretation."""
    return count_valid_passwords(filename, is_valid_p2)


def count_valid_passwords(filename, is_valid):
    """Count the number of valid passwords as per the `is_valid` function."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    return sum([is_valid(*regex.search(line).groups()) for line in lines])


def is_valid_p1(num_1, num_2, char, password):
    """Check whether the password is valid with the old policy interpretation."""
    return int(num_1) <= password.count(char) <= int(num_2)


def is_valid_p2(num_1, num_2, char, password):
    """Check whether the password is valid with the new policy interpretation."""
    return (password[int(num_1) - 1] == char) != (password[int(num_2) - 1] == char)


if __name__ == "__main__":
    main()

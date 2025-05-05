"""Solution --- Day 4: Secure Container ---"""

from itertools import pairwise

from advent_of_code.commons import tools

NR_DIGITS = 6


def main():
    filename = "input.txt"
    nr_valid = solve_p1(filename)
    print(f"P1: within the range, {nr_valid} passwords meet the original criteria.")
    nr_valid = solve_p2(filename)
    print(f"P2: within the range, {nr_valid} passwords meet the updated criteria.")


def solve_p1(filename):
    """Count the number of valid passwords under the original criteria."""
    return solve(filename, is_valid_p1)


def solve_p2(filename):
    """Count the number of valid passwords under the updated criteria."""
    return solve(filename, is_valid_p2)


def solve(filename, is_valid):
    """Count the number of valid non-decreasing passwords as per `is_valid`."""
    start, stop = parse_range_endpoints(filename)
    return sum([is_valid(pw) for pw in generate_nondecreasing_passwords(start, stop)])


def parse_range_endpoints(filename):
    """Convert start and stop of the range to lists of digits."""
    endpoints = tools.read_stripped(__file__, filename).split("-")
    assert all([len(endpoint) == NR_DIGITS for endpoint in endpoints])
    return [[int(x) for x in endpoint] for endpoint in endpoints]


def is_valid_p1(password):
    """Check whether the password contains a group of matching digits."""
    for digit_1, digit_2 in pairwise(password):
        if digit_1 == digit_2:
            return True
    return False


def is_valid_p2(password):
    """Check whether the password contains a group of exactly two matching digits."""
    group_len = 1
    for digit_1, digit_2 in pairwise(password):
        if digit_1 == digit_2:
            group_len += 1
            continue
        if group_len == 2:
            return True
        group_len = 1
    return group_len == 2


def generate_nondecreasing_passwords(start, stop):
    """Generate non-decreasing six-digit lists between start and stop (inclusive)."""
    password = start.copy()

    # Initialize the first non-decreasing list:
    for i in range(NR_DIGITS - 1):
        if password[i] > password[i + 1]:
            for j in range(i + 1, NR_DIGITS):
                password[j] = password[i]
            break

    # Iteratively yield non-decreasing lists in the given range:
    while password < stop:
        yield password
        i = NR_DIGITS - 1
        while password[i] == 9:
            i -= 1
        password[i] += 1
        for j in range(i + 1, NR_DIGITS):
            password[j] = password[i]
    if password == stop:
        yield password


if __name__ == "__main__":
    main()

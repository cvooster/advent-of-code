"""Solution --- Day 2: Inventory Management System ---"""

from collections import Counter
from itertools import combinations

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    checksum = solve_p1(filename)
    print(f"P1: the checksum for the list of box IDs is {checksum}.")
    letters = solve_p2(filename)
    print(f"P2: the common letters between the two box IDs are {letters}.")


def solve_p1(filename):
    """Multiply the numbers of IDs that have letters occur twice and thrice."""
    box_lines = tools.read_stripped_lines(__file__, filename)
    count_2 = 0
    count_3 = 0
    for line in box_lines:
        c = Counter(line)
        count_2 += 2 in c.values()
        count_3 += 3 in c.values()
    return count_2 * count_3


def solve_p2(filename):
    """Find common letters between the correct pair of boxes."""
    box_lines = tools.read_stripped_lines(__file__, filename)
    for box_1, box_2 in combinations(box_lines, r=2):
        if is_correct_pair(box_1, box_2):
            return get_common_letters(box_1, box_2)
    raise RuntimeError("The two correct boxes are not found!")


def is_correct_pair(box_1, box_2):
    """Check whether the two boxes differ by exactly one character."""
    saw_difference = False
    for char_1, char_2 in zip(box_1, box_2):
        if char_1 != char_2:
            if saw_difference:
                return False
            saw_difference = True
    return True


def get_common_letters(box_1, box_2):
    """Construct a string with the common characters of two boxes."""
    common = [char_1 for char_1, char_2 in zip(box_1, box_2) if char_1 == char_2]
    return "".join(common)


if __name__ == "__main__":
    main()

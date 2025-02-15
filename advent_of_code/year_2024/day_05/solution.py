"""Solution --- Day 5: Print Queue ---

This solution assumes that for every update, the page ordering rules induce a strict
total order with respect to its page numbers.

(A more general solution would be able to guarantee the correct answer for all sets of
page ordering rules that, for every update, induce a homogeneous binary relation that
can be uniquely extended into a total order. Such a solution would perform a topological
sort on the directed graph whose vertices correspond to page numbers of an update and
whose arcs correspond to page ordering rules; a unique topological ordering would exist,
giving the correct ordering of the update. Note: 'correct ordering' would not be well
defined for other page ordering rules.)
"""

from functools import cmp_to_key

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    page_sum = solve_p1(filename)
    print(f"P1: the middle page numbers of correct updates sum to {page_sum}.")
    page_sum = solve_p2(filename)
    print(f"P2: the middle page numbers of the corrected updates sum to {page_sum}.")


def solve_p1(filename):
    """Sum middle page numbers of correctly-ordered updates."""
    return solve(filename, True)


def solve_p2(filename):
    """Sum corrected middle page numbers of incorrectly-ordered updates."""
    return solve(filename, False)


def solve(filename, flag_correctness):
    """Sum (corrected) middle page numbers of (in)correctly-ordered updates."""
    updates, order_dict = initialize_updates_and_orderings(filename)
    sorted_updates = sort_updates(updates, order_dict)
    total = 0
    for update, sorted_update in zip(updates, sorted_updates):
        if (update == sorted_update) == flag_correctness:
            total += sorted_update[len(sorted_update) // 2]
    return total


def initialize_updates_and_orderings(filename):
    """Parse input, and return an update list and an ordering dictionary."""
    lines = tools.read_stripped(__file__, filename)
    order_lines, update_lines = [x.split("\n") for x in lines.split("\n\n")]

    order_dict = {}
    for line in order_lines:
        left, right = [int(x) for x in line.split("|")]
        order_dict[(left, right)] = -1
        order_dict[(right, left)] = 1

    updates = [[int(x) for x in line.split(",")] for line in update_lines]
    if any(len(update) % 2 == 0 for update in updates):
        raise AssertionError("Update has an even length, and no middle page!")
    return updates, order_dict


def sort_updates(updates, order_dict):
    """Create a list of correctly ordered updates."""

    def compare(page_number_1, page_number_2):
        """Return -1 or 1 for `page_number_1` before or after `page_number_2`."""
        return order_dict[(page_number_1, page_number_2)]

    # The following comparison sort is guaranteed to return the correct answer if the
    # assumption made by this solution is valid. Otherwise, it may throw a key error or
    # return an incorrect answer:
    return [sorted(update, key=cmp_to_key(compare)) for update in updates]


if __name__ == "__main__":
    main()

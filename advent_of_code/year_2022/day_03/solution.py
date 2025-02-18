"""Solution --- Day 3: Rucksack Reorganization ---"""

from advent_of_code.commons import tools

GROUP_SIZE = 3


def main():
    filename = "input.txt"
    priority_sum = solve_p1(filename)
    print(f"P1: the priorities of two-compartment item types sum to {priority_sum}.")
    priority_sum = solve_p2(filename)
    print(f"P2: the priorities of the badge item types sum to {priority_sum}.")


def solve_p1(filename):
    """Sum the priorities of items that appear in two compartments."""
    rucksacks = tools.read_stripped_lines(__file__, filename)
    return sum(assign_priority(get_item_type(rucksack)) for rucksack in rucksacks)


def solve_p2(filename):
    """Sum the priorities of the badge item types."""
    rucksacks = tools.read_stripped_lines(__file__, filename)
    if len(rucksacks) % GROUP_SIZE != 0:
        raise ValueError(f"Number of rucksacks not a multiple of {GROUP_SIZE}!")
    priority_sum = 0
    for i in range(0, len(rucksacks), GROUP_SIZE):
        priority_sum += assign_priority(get_badge(rucksacks[i : i + GROUP_SIZE]))
    return priority_sum


def get_item_type(rucksack):
    """For a given rucksack, get the item type that appears in both compartments."""
    if len(rucksack) % 2 != 0:
        raise ValueError("A rucksack contains an odd number of items!")
    compartment_1 = rucksack[: len(rucksack) // 2]
    compartment_2 = rucksack[len(rucksack) // 2 :]
    duplicate_types = set(compartment_1) & set(compartment_2)
    if len(duplicate_types) != 1:
        raise AssertionError(f"A rucksack has {len(duplicate_types)} shared types!")
    return duplicate_types.pop()


def get_badge(rucksack_group):
    """Get the item type that appears in all rucksacks in a given group."""
    rucksack_sets = [set(rucksack) for rucksack in rucksack_group]
    common_items = set.intersection(*rucksack_sets)
    if len(common_items) != 1:
        raise ValueError(f"A group has {len(common_items)} item types in common!")
    return common_items.pop()


def assign_priority(item_type):
    """Convert an item type to a priority."""
    return ord(item_type) - 96 if item_type.islower() else ord(item_type) - 38


if __name__ == "__main__":
    main()

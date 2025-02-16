"""Solution --- Day 4: Scratchcards ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    point_sum = solve_p1(filename)
    print(f"P1: the pile of scratchcards is worth {point_sum} points.")
    nr_instances = solve_p2(filename)
    print(f"P2: the process results in {nr_instances} scratchcards.")


def solve_p1(filename):
    """Evaluate the numbers of matches, and sum all points."""
    card_lines = tools.read_stripped_lines(__file__, filename)
    point_sum = 0
    for line in card_lines:
        nr_winners = determine_winners(line)
        if nr_winners > 0:
            point_sum += 2 ** (nr_winners - 1)
    return point_sum


def solve_p2(filename):
    """Evaluate the numbers of matches, and get the total number of scratchcards."""
    card_lines = tools.read_stripped_lines(__file__, filename)
    nrs_instances = [1] * len(card_lines)
    for i, line in enumerate(card_lines):
        nr_winners = determine_winners(line)
        if nr_winners >= len(card_lines) - i:
            raise AssertionError("Attempt to copy a card past the end of the table!")
        for j in range(i + 1, i + 1 + nr_winners):
            nrs_instances[j] += nrs_instances[i]
    return sum(nrs_instances)


def determine_winners(line):
    """Evaluate the number of matches for the scratchcard on the given line."""
    number_list_1, number_list_2 = line.split("|")
    winning = set(number_list_1.split()[2:])
    on_card = set(number_list_2.split())
    return len(winning & on_card)


if __name__ == "__main__":
    main()

"""Solution --- Day 1: Calorie Counting ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    max_total = solve_p1(filename)
    print(f"P1: the maximum calorie total carried by an elf is {max_total}.")
    top_totals_sum = solve_p2(filename)
    print(f"P2: the sum of the top-three calorie totals is {top_totals_sum}.")


def solve_p1(filename):
    """Determine the maximum calorie total carried by an elf."""
    return sum_top_totals(filename, 1)


def solve_p2(filename):
    """Sum the calories carried by the elves with the three highest totals."""
    return sum_top_totals(filename, 3)


def sum_top_totals(filename, cut_off_rank):
    """Sum the calories carried by the elves with the `cut_off_rank`-highest totals."""
    calorie_groups = tools.read_stripped(__file__, filename).split("\n\n")
    totals = [sum(int(x) for x in group.split("\n")) for group in calorie_groups]
    sorted_totals = sorted(totals)
    if cut_off_rank > len(sorted_totals):
        return ValueError("The cut-off rank exceeds the number of elves!")
    return sum(sorted_totals[-cut_off_rank:])


if __name__ == "__main__":
    main()

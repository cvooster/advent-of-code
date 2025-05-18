"""Solution --- Day 6: Custom Customs ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    count_sum = solve_p1(filename)
    print(f"P1: the counts of questions answered 'yes' by anyone sum to {count_sum}.")
    count_sum = solve_p2(filename)
    print(f"P2: the counts of questions answered 'yes' by everyone sum to {count_sum}.")


def solve_p1(filename):
    """Count and sum the numbers of questions to which anyone answered 'yes'."""
    lines = tools.read_stripped(__file__, filename)
    return sum([count_anyone(group) for group in lines.split("\n\n")])


def solve_p2(filename):
    """Count and sum the number of questions to which everyone answered 'yes'."""
    lines = tools.read_stripped(__file__, filename)
    return sum([count_everyone(group) for group in lines.split("\n\n")])


def count_anyone(group):
    """For the given group, count questions to which anyone answered 'yes'."""
    return len(set.union(*[set(line) for line in group.split("\n")]))


def count_everyone(group):
    """For the given group, count questions to which everyone answered 'yes'."""
    return len(set.intersection(*[set(line) for line in group.split("\n")]))


if __name__ == "__main__":
    main()

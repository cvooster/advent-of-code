"""Solution --- Day 1: Historian Hysteria ---"""

from collections import Counter

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    distance = solve_p1(filename)
    print(f"P1: the total distance between the two lists is {distance}.")
    similarity = solve_p2(filename)
    print(f"P2: the similarity score of the two lists is {similarity}.")


def solve_p1(filename):
    """Compute the total distance between the left and right location IDs."""
    lines = tools.read_stripped_lines(__file__, filename)
    lefts, rights = list(zip(*[[int(x) for x in line.split()] for line in lines]))
    return sum(abs(id_2 - id_1) for id_1, id_2 in zip(sorted(lefts), sorted(rights)))


def solve_p2(filename):
    """Compute the similarity score of the left and right location IDs."""
    lines = tools.read_stripped_lines(__file__, filename)
    lefts, rights = list(zip(*[[int(x) for x in line.split()] for line in lines]))
    counts_left, counts_right = Counter(lefts), Counter(rights)
    return sum(id_ * counts_right[id_] * counts_left[id_] for id_ in counts_left)


if __name__ == "__main__":
    main()

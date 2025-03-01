"""Solution --- Day 1: Not Quite Lisp ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    floor = solve_p1(filename)
    print(f"P1: the instructions take Santa to floor {floor}.")
    position = solve_p2(filename)
    print(f"P2: the first entrance is caused by the character at position {position}.")


def solve_p1(filename):
    """Determine the floor where Santa ends up."""
    directions = tools.read_stripped(__file__, filename)
    return len(directions) - 2 * directions.count(")")


def solve_p2(filename):
    """Determine the first entrance time for the basement."""
    directions = tools.read_stripped(__file__, filename)
    floor = 0
    for i, char in enumerate(directions, start=1):
        floor = floor + 1 - 2 * (char == ")")
        if floor == -1:
            return i
    raise RuntimeError("The basement is never entered!")


if __name__ == "__main__":
    main()

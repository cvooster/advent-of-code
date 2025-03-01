"""Solution --- Day 3: Perfectly Spherical Houses in a Vacuum ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_houses = solve_p1(filename)
    print(f"P1: {nr_houses} houses receive at least one present.")
    nr_houses = solve_p2(filename)
    print(f"P2: with Robo-Santa, {nr_houses} houses receive at least one present.")


def solve_p1(filename):
    """Determine houses to receive at least one present from Santa."""
    directions = tools.read_stripped(__file__, filename)
    deliveries = visit_houses(directions, set())
    return len(deliveries)


def solve_p2(filename):
    """Determine houses to receive at least one present from (Robo-)Santa."""
    directions = tools.read_stripped(__file__, filename)
    deliveries = visit_houses(directions[0::2], set())
    deliveries = visit_houses(directions[1::2], deliveries)
    return len(deliveries)


def visit_houses(directions, deliveries):
    """Deliver presents, and construct a set of visited coordinates."""
    x, y = 0, 0
    deliveries.add((x, y))
    # Throughout, x and y coordinates are relative to the starting position:
    for char in directions:
        x, y = move(x, y, char)
        deliveries.add((x, y))
    return deliveries


def move(x, y, char):
    """Move to new x- and y-coordinates following `char` instruction."""
    if char == "^":
        return x, y + 1
    elif char == ">":
        return x + 1, y
    elif char == "<":
        return x - 1, y
    elif char == "v":
        return x, y - 1


if __name__ == "__main__":
    main()

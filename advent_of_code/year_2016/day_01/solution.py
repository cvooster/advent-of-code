"""Solution --- Day 1: No Time for a Taxicab ---

Directions are encoded by 0 for North, 1 for East, 2 for South, and 3 for West.
"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    distance = solve_p1(filename)
    print(f"P1: with the initial instructions, HQ is {distance} blocks away.")
    distance = solve_p2(filename)
    print(f"P2: with the updated instructions, HQ is {distance} blocks away.")


def solve_p1(filename):
    """Determine the destination for the given instructions."""
    moves = tools.read_stripped(__file__, filename).split(", ")
    x, y, direction = 0, 0, 0
    for move in moves:
        turn, move_size = move[0], int(move[1:])
        direction = take_turn(direction, turn)
        x, y = walk_forward(x, y, direction, move_size)
    return abs(x) + abs(y)


def solve_p2(filename):
    """Determine the first revisited location for the given instructions."""
    moves = tools.read_stripped(__file__, filename).split(", ")
    x, y, direction = 0, 0, 0
    visited = {(x, y)}
    for move in moves:
        turn, move_size = move[0], int(move[1:])
        direction = take_turn(direction, turn)
        x, y = walk_forward(x, y, direction, move_size)
        locations = get_new_visited(x, y, direction, move_size)
        # Check whether this move revisits a location:
        for x_, y_ in locations:
            if (x_, y_) in visited:
                return abs(x_) + abs(y_)
        # Extend the set of visited locations:
        visited |= set(locations)
    raise RuntimeError("No location is visited twice!")


def take_turn(direction, turn):
    """Given a current direction return the direction after `turn` is made."""
    return (direction - 1) % 4 if turn == "L" else (direction + 1) % 4


def walk_forward(x, y, direction, move_size):
    """From x, y, walk `move_size` blocks in the given direction."""
    if direction == 0:
        return x, y + move_size
    elif direction == 1:
        return x + move_size, y
    elif direction == 2:
        return x, y - move_size
    elif direction == 3:
        return x - move_size, y


def get_new_visited(x, y, direction, move_size):
    """Get `move_size` locations on the way to x, y, walking in the given direction."""
    if direction == 0:
        return [(x, y_) for y_ in range(y, y - move_size, -1)]
    elif direction == 1:
        return [(x_, y) for x_ in range(x, x - move_size, -1)]
    elif direction == 2:
        return [(x, y_) for y_ in range(y, y + move_size)]
    elif direction == 3:
        return [(x_, y) for x_ in range(x, x + move_size)]


if __name__ == "__main__":
    main()

"""Solution --- Day 5: A Maze of Twisty Trampolines, All Alike ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_steps = solve_p1(filename)
    print(f"P1: with the original offset updating rule, it takes {nr_steps} steps.")
    nr_steps = solve_p2(filename)
    print(f"P2: with the new offset updating rule, it takes {nr_steps} steps.")


def solve_p1(filename):
    """Determine the number of steps to exit the maze under the original rule."""
    return reach_exit(filename, update_p1)


def solve_p2(filename):
    """Determine the number of steps to exit the maze under the new rule."""
    return reach_exit(filename, update_p2)


def reach_exit(filename, update):
    """Jump through the maze until an exit is reached."""
    offsets = [int(x) for x in tools.read_stripped_lines(__file__, filename)]
    maze_len = len(offsets)
    index = 0
    nr_steps = 0
    while 0 <= index < maze_len:
        current_offset = offsets[index]
        offsets[index] = update(offsets[index])
        index += current_offset
        nr_steps += 1
    return nr_steps


def update_p1(offset):
    """Get updated offset value according to the original rule."""
    return offset + 1


def update_p2(offset):
    """Get updated offset value according to the new rule."""
    return offset + 1 if offset < 3 else offset - 1


if __name__ == "__main__":
    main()

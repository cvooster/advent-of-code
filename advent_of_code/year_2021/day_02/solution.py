"""Solution --- Day 2: Dive! ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    final_product = solve_p1(filename)
    print(f"P1: the part-1 position and depth multiply to {final_product}.")
    final_product = solve_p2(filename)
    print(f"P2: the part-2 position and depth multiply to {final_product}.")


def solve_p1(filename):
    """Simulate submarine dive according to the part-1 instructions."""
    command_lines = tools.read_stripped_lines(__file__, filename)
    horizontal_pos = 0
    depth = 0
    for line in command_lines:
        direction, magnitude = line.split()
        if direction == "forward":
            horizontal_pos += int(magnitude)
        elif direction == "down":
            depth += int(magnitude)
        elif direction == "up":
            depth -= int(magnitude)
    return horizontal_pos * depth


def solve_p2(filename):
    """Simulate submarine dive according to the part-2 instructions."""
    command_lines = tools.read_stripped_lines(__file__, filename)
    horizontal_pos = 0
    depth, aim = 0, 0
    for line in command_lines:
        direction, magnitude = line.split()
        if direction == "forward":
            horizontal_pos += int(magnitude)
            depth += aim * int(magnitude)
        elif direction == "down":
            aim += int(magnitude)
        elif direction == "up":
            aim -= int(magnitude)
    return horizontal_pos * depth


if __name__ == "__main__":
    main()

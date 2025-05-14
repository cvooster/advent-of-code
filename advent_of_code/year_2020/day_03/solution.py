"""Solution --- Day 3: Toboggan Trajectory ---"""

import math

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_trees = solve_p1(filename)
    print(f"P1: the number of trees on the given slope is {nr_trees}.")
    nr_trees = solve_p2(filename)
    print(f"P2: the numbers of trees on the listed slopes multiply to {nr_trees}.")


def solve_p1(filename):
    """Count the number of trees on the slope right 3, down 1."""
    return count_and_multiply(filename, [(3, 1)])


def solve_p2(filename):
    """Count and multiply the numbers of trees on a list of five different slopes."""
    return count_and_multiply(filename, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


def count_and_multiply(filename, slopes):
    """Read the map, and count and multiply the numbers of trees on the given slopes."""
    grid_lines, grid_height, grid_width = initialize_grid(filename)
    nrs = [count_trees(grid_lines, grid_height, grid_width, *d) for d in slopes]
    return math.prod(nrs)


def initialize_grid(filename):
    """Read file input, and obtain the grid height and width of the tree map."""
    grid_lines = tools.read_stripped_lines(__file__, filename)
    return grid_lines, len(grid_lines), len(grid_lines[0])


def count_trees(grid_lines, grid_height, grid_width, dx, dy):
    """Count the number of trees encountered on the slope right `dx`, down `dy`."""
    nr_trees = 0
    pos_y, pos_x = 0, 0
    while pos_y < grid_height:
        nr_trees += grid_lines[pos_y][pos_x] == "#"
        pos_y += dy
        pos_x = (pos_x + dx) % grid_width
    return nr_trees


if __name__ == "__main__":
    main()

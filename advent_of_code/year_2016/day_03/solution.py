"""Solution --- Day 3: Squares With Three Sides ---"""

from itertools import batched, chain

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_valid = solve_p1(filename)
    print(f"P1: {nr_valid} lines specify valid triangles.")
    nr_valid = solve_p2(filename)
    print(f"P2: {nr_valid} three-number sets specify valid triangles.")


def solve_p1(filename):
    """Count the number of lines that specify valid triangles."""
    triangle_lines = tools.read_stripped_lines(__file__, filename)
    triangles = [[int(x) for x in line.split()] for line in triangle_lines]
    return sum([is_valid(triangle) for triangle in triangles])


def solve_p2(filename):
    """Count the number of vertical three-number sets that specify valid triangles."""
    triangle_lines = tools.read_stripped_lines(__file__, filename)
    numbers = [[int(x) for x in line.split()] for line in triangle_lines]
    if len(numbers) % 3 != 0:
        raise AssertionError("Input is not vertically divisible into groups of three!")
    triangles = list(batched(chain.from_iterable(zip(*numbers)), 3))
    return sum([is_valid(triangle) for triangle in triangles])


def is_valid(triangle):
    """Check whether a triangle specification is valid."""
    sorted_triangle = sorted(triangle)
    return sorted_triangle[0] + sorted_triangle[1] > sorted_triangle[2]


if __name__ == "__main__":
    main()

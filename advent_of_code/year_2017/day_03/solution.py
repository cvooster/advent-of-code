"""Solution --- Day 3: Spiral Memory ---"""

from collections import defaultdict
import math

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    steps = solve_p1(filename)
    print(f"P1: it takes {steps} steps to carry the data to the access port.")
    value = solve_p2(filename)
    print(f"P2: the first value written larger than the threshold is {value}.")


def solve_p1(filename):
    """Compute the Manhattan distance from the access port to the input square.

    Determine the smallest odd integer n such that the n x n grid with the access port
    at its center contains the input square. Decompose the distance into the distance
    from access port to the midpoint of the 'edge' on which the square is located and
    the distance from the 'edge' midpoint to the square, and compute both distances in
    terms of n.
    """
    square_number = int(tools.read_stripped(__file__, filename))
    n = compute_edge_length(square_number)
    return compute_distance_to_edge(n) + compute_distance_on_edge(square_number, n)


def solve_p2(filename):
    """Determine the first value larger than a threshold during the stress test.

    This function breaks the iterative process down into determining values for the
    edges of n x n grids, for increasing values of n (equivalently, `distance_to_edge`).
    It is then further broken down into the right, top, left, and bottom edges, using
    specific adjacency directions for each side.
    """
    threshold = int(tools.read_stripped(__file__, filename))
    square_values = defaultdict(int)
    square_values[(0, 0)] = 1

    # Directions of adjacent squares, for each edge side:
    # fmt: off
    directions = {
        "R": [(-1, -1), (-1,  0), (-1,  1),  (0, -1)],
        "T": [(-1, -1),  (0, -1),  (1, -1),  (1,  0)],
        "L":  [(1,  1),  (1,  0),  (1, -1),  (0,  1)],
        "B": [(-1,  1),  (0,  1),  (1,  1), (-1,  0)],
    }
    # fmt: on

    distance_to_edge = 0
    while True:
        distance_to_edge += 1
        coordinates = get_edge_coordinates(distance_to_edge)
        for side in "RTLB":
            adjacent = directions[side]
            # Allocate values to each coordinate on the edge at the given side:
            for x, y in coordinates[side]:
                value = sum(square_values[(x + dx, y + dy)] for dx, dy in adjacent)
                if value > threshold:
                    return value
                square_values[(x, y)] = value


def compute_edge_length(square_number):
    """Compute smallest odd n such that n x n grid contains the given square number."""
    n = math.ceil(math.sqrt(square_number))
    return n if n % 2 == 1 else n + 1


def compute_distance_to_edge(n):
    """Compute the number of steps from access port to edge of n x n grid."""
    return n // 2


def compute_distance_on_edge(square_number, n):
    """Compute the number of steps from a square on the edge of n x n grid to midpoint.

    On an n x n grid, it takes n - 1 steps from one cornerpoint to the next one. Hence,
    the number of steps from a square on the edge to the next cornerpoint is at least 0
    and (if n > 1) at most n - 2. By determining this number and subtracting the number
    of steps from cornerpoint to edge midpoint, one gets the number of steps to the
    midpoint or (if the difference is negative) past the midpoint.
    """
    distance_to_next_cornerpoint = (n**2 - square_number) % (n - 1) if n > 1 else 0
    return abs(distance_to_next_cornerpoint - n // 2)


def get_edge_coordinates(distance):
    """Get edge coordinates by side for a grid with the given distance to the edges."""
    return {
        "R": [(distance, y) for y in range(-distance + 1, distance + 1)],
        "T": [(x, distance) for x in range(distance - 1, -distance - 1, -1)],
        "L": [(-distance, y) for y in range(distance - 1, -distance - 1, -1)],
        "B": [(x, -distance) for x in range(-distance + 1, distance + 1)],
    }


if __name__ == "__main__":
    main()

"""Solution --- Day 3: Crossed Wires ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    distance = solve_p1(filename)
    print(f"P1: the Manhattan distance to the closest intersection is {distance}.")
    nr_steps = solve_p2(filename)
    print(f"P2: the fewest combined steps to reach an intersection is {nr_steps}.")


def solve_p1(filename):
    """Determine the distance from the central port to the closest intersection."""
    visited = setup_wire_paths(filename)
    intersections = visited[0].keys() & visited[1].keys()
    return min([abs(key[0]) + abs(key[1]) for key in intersections])


def solve_p2(filename):
    """Determine the minimum number of combined steps to an intersection."""
    visited = setup_wire_paths(filename)
    intersections = visited[0].keys() & visited[1].keys()
    return min([visited[0][key] + visited[1][key] for key in intersections])


def setup_wire_paths(filename):
    """Create dictionaries with the points and number of steps for the two wires."""
    lines = tools.read_stripped_lines(__file__, filename)
    return map_wire_path(lines[0]), map_wire_path(lines[1])


def map_wire_path(line):
    """Create a dictionary with all points on the wire path, with number of steps."""
    visited = {}
    y, x, steps = 0, 0, 0
    for move in line.split(","):
        direction, magnitude = move[0], int(move[1:])

        if direction == "U":
            for y_ in range(y + 1, y + magnitude + 1):
                steps += 1
                if (y_, x) not in visited:
                    visited[(y_, x)] = steps
            y += magnitude

        elif direction == "D":
            for y_ in range(y - 1, y - magnitude - 1, -1):
                steps += 1
                if (y_, x) not in visited:
                    visited[(y_, x)] = steps
            y -= magnitude

        elif direction == "L":
            for x_ in range(x - 1, x - magnitude - 1, -1):
                steps += 1
                if (y, x_) not in visited:
                    visited[(y, x_)] = steps
            x -= magnitude

        elif direction == "R":
            for x_ in range(x + 1, x + magnitude + 1):
                steps += 1
                if (y, x_) not in visited:
                    visited[(y, x_)] = steps
            x += magnitude
    return visited


if __name__ == "__main__":
    main()

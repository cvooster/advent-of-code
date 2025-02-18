"""Solution --- Day 1: Sonar Sweep ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_increments = solve_p1(filename)
    print(f"P1: {nr_increments} measurements are larger than the previous one.")
    nr_increments = solve_p2(filename)
    print(f"P2: {nr_increments} moving sums are larger than the previous one.")


def solve_p1(filename):
    """Count the number of increments in the measurements."""
    return count_lagged_increments(filename, 1)


def solve_p2(filename):
    """Count the number of increments in three-measurement moving sums."""
    return count_lagged_increments(filename, 3)


def count_lagged_increments(filename, lag):
    """Count the number of measurements larger than a lagged version of itself."""
    depth_lines = tools.read_stripped_lines(__file__, filename)
    depths = [int(x) for x in depth_lines]
    return sum(depths[i] > depths[i - lag] for i in range(lag, len(depths)))


if __name__ == "__main__":
    main()

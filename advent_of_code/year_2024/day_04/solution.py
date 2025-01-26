"""Solution --- Day 4: Ceres Search ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    count = solve_p1(filename)
    print(f"P1: XMAS appears {count} times in the word search.")
    count = solve_p2(filename)
    print(f"P2: X-MAS appears {count} times in the word search.")


def solve_p1(filename):
    """Count the number of XMAS occurrences in the word search."""
    grid, grid_height, grid_width = initialize_grid(filename)
    pattern = ["X", "M", "A", "S"]
    pat_len = len(pattern)

    count = 0
    for i in range(grid_height):
        for j in range(grid_width):
            # A necessary condition for the pattern to occur in any direction starting
            # from the letter in the i-th row and j-th column is that this is the first
            # letter of the pattern:
            if grid[i][j] != pattern[0]:
                continue
            # Now, scan eight directions:
            for di in (-1, 0, 1):
                if not 0 <= i + di * (pat_len - 1) < grid_height:
                    continue
                for dj in (-1, 0, 1):
                    if not 0 <= j + dj * (pat_len - 1) < grid_width:
                        continue
                    if di == dj == 0:
                        continue
                    letters = [grid[i + n * di][j + n * dj] for n in range(pat_len)]
                    count += letters == pattern
    return count


def solve_p2(filename):
    """Count the number of occurrences of X-MAS in the word search."""
    grid, grid_height, grid_width = initialize_grid(filename)
    middle_point = "A"
    cornerpoints = (
        ["M", "M", "S", "S"],  # up left, up right, down left, down right
        ["M", "S", "M", "S"],
        ["S", "S", "M", "M"],
        ["S", "M", "S", "M"],
    )

    count = 0
    for i in range(1, grid_height - 1):
        for j in range(1, grid_width - 1):
            # Check the letter in the i-th row and j-th column as a possible center:
            if not grid[i][j] == middle_point:
                continue
            # Next, check the diagonally adjacent letters:
            letters = [grid[m][n] for m in (i - 1, i + 1) for n in (j - 1, j + 1)]
            count += letters in cornerpoints
    return count


def initialize_grid(filename):
    """Read file input, and initialize the word search grid."""
    lines = tools.read_stripped_lines(__file__, filename)
    grid = [[char for char in line] for line in lines]
    return grid, len(grid), len(grid[0])


if __name__ == "__main__":
    main()

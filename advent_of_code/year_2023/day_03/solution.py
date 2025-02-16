"""Solution --- Day 3: Gear Ratios ---"""

import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    part_number_sum = solve_p1(filename)
    print(f"P1: the part numbers in the engine schematic sum to {part_number_sum}.")
    gear_ratio_sum = solve_p2(filename)
    print(f"P2: the gear ratios in the engine schematic sum to {gear_ratio_sum}.")


def solve_p1(filename):
    """Identify all part numbers in the engine schematic, and take their sum."""
    grid_lines, grid_height, grid_width = initialize_grid(filename)
    located_by_row = search_all_numbers(grid_lines)

    part_numbers_by_position = {}
    for i in range(grid_height):
        for j in range(grid_width):
            if grid_lines[i][j] != "." and not grid_lines[i][j].isnumeric():
                # Numbers adjacent to the current position are part numbers.
                part_numbers_by_position |= get_adjacent_numbers(located_by_row, i, j)
    return sum(part_numbers_by_position.values())


def solve_p2(filename):
    """Identify all gears in the engine schematic, and sum their ratios."""
    grid_lines, grid_height, grid_width = initialize_grid(filename)
    located_by_row = search_all_numbers(grid_lines)

    gear_ratio_sum = 0
    for i in range(grid_height):
        for j in range(grid_width):
            if grid_lines[i][j] == "*":
                numbers_by_position = get_adjacent_numbers(located_by_row, i, j)
                if len(numbers_by_position) == 2:
                    # The * symbol is a gear.
                    part_number_1, part_number_2 = numbers_by_position.values()
                    gear_ratio_sum += part_number_1 * part_number_2
    return gear_ratio_sum


def initialize_grid(filename):
    """Read file input, and obtain the grid height and width of the engine schematic."""
    grid_lines = tools.read_stripped_lines(__file__, filename)
    return grid_lines, len(grid_lines), len(grid_lines[0])


def search_all_numbers(grid_lines):
    """Construct a list of lists with located numbers at every row."""
    located_by_row = []
    for line in grid_lines:
        # Construct a list of tuples of the form (start index, end index, value):
        located = [(*m.span(), int(m.group())) for m in re.finditer(r"\d+", line)]
        located_by_row.append(located)
    return located_by_row


def get_adjacent_numbers(located_by_row, i, j):
    """Get dictionary with position-value pairs for numbers adjacent to i, j."""
    adjacent_numbers = {}
    for i_ in range(i - 1, i + 2):
        for start_idx, end_idx, value in located_by_row[i_]:
            # A number is adjacent if the start index is smaller than or equal to j + 1
            # and the end index is greater than or equal to j. Because of the ordering
            # used in the construction of `located_by_row[i_]`, once a number has a
            # start index greater than j + 1, no subsequent number can be adjacent.
            if start_idx > j + 1:
                break
            elif end_idx >= j:
                adjacent_numbers[(i_, start_idx)] = value
    return adjacent_numbers


if __name__ == "__main__":
    main()

"""Solution --- Day 1: Trebuchet?! ---"""

from advent_of_code.commons import tools

WORDS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
NUMBERS = {k: i + 1 for i, k in enumerate(WORDS)}


def main():
    filename = "input.txt"
    value_sum = solve_p1(filename)
    print(f"P1: the calibration values add up to {value_sum} in part 1.")
    value_sum = solve_p2(filename)
    print(f"P2: the calibration values add up to {value_sum} in part 2.")


def solve_p1(filename):
    """For part 1, sum the recovered calibration values."""
    lines = tools.read_stripped_lines(__file__, filename)
    return sum(10 * get_first_digit(line) + get_last_digit(line) for line in lines)


def solve_p2(filename):
    """For part 2, sum the recovered calibration values."""
    lines = tools.read_stripped_lines(__file__, filename)
    return sum(10 * get_first_numeral(line) + get_last_numeral(line) for line in lines)


def get_first_digit(line):
    """Get the first digit on a line."""
    return int(next(char for char in line if char.isnumeric()))


def get_last_digit(line):
    """Get the last digit on a line."""
    return int(next(char for char in reversed(line) if char.isnumeric()))


def get_first_numeral(line):
    """Get the first digit or spelled out digit on a line."""
    for i, char in enumerate(line):
        if char.isnumeric():
            return int(char)
        line_start = line[: i + 1]
        for word, value in NUMBERS.items():
            if word in line_start:
                return value


def get_last_numeral(line):
    """Get the last digit or spelled out digit on a line."""
    for i, char in enumerate(reversed(line)):
        if char.isnumeric():
            return int(char)
        line_end = line[-i - 1 :]
        for word, value in NUMBERS.items():
            if word in line_end:
                return value


if __name__ == "__main__":
    main()

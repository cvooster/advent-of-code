"""Solution --- Day 2: Corruption Checksum ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    checksum = solve_p1(filename)
    print(f"P1: the checksum for the spreadsheet is {checksum}.")
    division_sum = solve_p2(filename)
    print(f"P2: the results of the divisions sum to {division_sum}.")


def solve_p1(filename):
    """Calculate the spreadsheet's checksum."""
    spreadsheet_lines = tools.read_stripped_lines(__file__, filename)
    spreadsheet = [[int(x) for x in line.split()] for line in spreadsheet_lines]
    return sum(max(row) - min(row) for row in spreadsheet)


def solve_p2(filename):
    """Perform the division for each spreadsheet row, and sum the results."""
    spreadsheet_lines = tools.read_stripped_lines(__file__, filename)
    spreadsheet = [[int(x) for x in line.split()] for line in spreadsheet_lines]
    return sum(determine_quotient(row) for row in spreadsheet)


def determine_quotient(row):
    """Find the two numbers where one evenly divides the other, and get quotient."""
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] % row[j] == 0:
                return row[i] // row[j]
            if row[j] % row[i] == 0:
                return row[j] // row[i]
    raise RuntimeError("Row contains no two numbers satisfying the requirement!")


if __name__ == "__main__":
    main()

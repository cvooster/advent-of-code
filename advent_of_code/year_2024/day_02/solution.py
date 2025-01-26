"""Solution --- Day 2: Red-Nosed Reports ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_safe = solve_p1(filename)
    print(f"P1: under the original rules, {nr_safe} reports are safe.")
    nr_safe = solve_p2(filename)
    print(f"P2: under the new rules, {nr_safe} reports are safe.")


def solve_p1(filename):
    """Count the number of safe reports under the original rules."""
    lines = tools.read_stripped_lines(__file__, filename)
    reports = [[int(x) for x in line.split()] for line in lines]
    return sum(is_safe_p1(report) for report in reports)


def solve_p2(filename):
    """Count the number of safe reports under the new rules."""
    lines = tools.read_stripped_lines(__file__, filename)
    reports = [[int(x) for x in line.split()] for line in lines]
    return sum(is_safe_p2(report) for report in reports)


def is_safe_p1(report):
    """Determine whether a given report is safe under the original rules."""
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    is_gradually_decreasing = all(-3 <= d <= -1 for d in differences)
    is_gradually_increasing = all(1 <= d <= 3 for d in differences)
    return is_gradually_decreasing or is_gradually_increasing


def is_safe_p2(report):
    """Determine whether a given report is safe under the new rules."""
    return any(is_safe_p1(report[:j] + report[j + 1 :]) for j in range(len(report)))


if __name__ == "__main__":
    main()

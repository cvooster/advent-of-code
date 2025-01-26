"""Solution --- Day 3: Mull It Over ---"""

import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    output = solve_p1(filename)
    print(f"P1: the results of all multiplications add up to {output}.")
    output = solve_p2(filename)
    print(f"P2: the results of enabled multiplications add up to {output}.")


def solve_p1(filename):
    """Perform all multiplications, and sum the results."""
    line = tools.read_stripped(__file__, filename)
    multiplicands = re.findall(r"(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))", line)
    return sum(int(x) * int(y) for x, y in multiplicands)


def solve_p2(filename):
    """Perform only the enabled multiplications, and sum the results."""
    line = tools.read_stripped(__file__, filename)
    regex = re.compile(r"(?:(?<=mul\()(\d{1,3}),(\d{1,3})(?=\)))|(do\(\))|(don\'t\(\))")
    matches = re.findall(regex, line)

    # There are four capturing groups in the regular expression. Therefore, for each
    # uncorrupted instruction, a tuple with four strings is obtained. These strings are
    # non-empty (empty) if the match is (not) on their corresponding groups.

    total = 0
    enabled = True
    for match in matches:
        # Check which string is non-empty to determine the corresponding instruction:
        if match[2]:
            enabled = True
        elif match[3]:
            enabled = False
        else:
            # Multiplication is carried out only if it is enabled:
            if enabled:
                total += int(match[0]) * int(match[1])
    return total


if __name__ == "__main__":
    main()

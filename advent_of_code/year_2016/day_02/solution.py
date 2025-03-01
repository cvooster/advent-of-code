"""Solution --- Day 2: Bathroom Security ---"""

from advent_of_code.commons import tools

# fmt: off
SIMPLE_KEYPAD = (
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9")
)
DESIGN_KEYPAD = (
    (None, None, "1", None, None),
    (None, "2",  "3", "4",  None),
    ("5",  "6",  "7", "8",  "9"),
    (None, "A",  "B", "C",  None),
    (None, None, "D", None, None)
)
# fmt: on


def main():
    filename = "input.txt"
    code = solve_p1(filename)
    print(f"P1: the instructions result in {code} on the simple keypad.")
    code = solve_p2(filename)
    print(f"P2: the instructions result in {code} on the design keypad.")


def solve_p1(filename):
    """Determine the bathroom code for the simple keypad."""
    lines = tools.read_stripped_lines(__file__, filename)
    code = []
    i, j = 1, 1  # position of the "5" button
    for line in lines:
        i, j = move_to_next_button_p1(i, j, line)
        code.append(SIMPLE_KEYPAD[i][j])
    return "".join(code)


def solve_p2(filename):
    """Determine the bathroom code for the design keypad."""
    lines = tools.read_stripped_lines(__file__, filename)
    code = []
    i, j = 2, 0  # position of the "5" button
    for line in lines:
        i, j = move_to_next_button_p2(i, j, line)
        code.append(DESIGN_KEYPAD[i][j])
    return "".join(code)


def move_to_next_button_p1(i, j, line):
    """From i-th row and j-th column of the simple keypad, follow instruction line."""
    for char in line:
        if char == "U":
            if i > 0:
                i -= 1
        elif char == "L":
            if j > 0:
                j -= 1
        elif char == "D":
            if i < 2:
                i += 1
        elif char == "R":
            if j < 2:
                j += 1
    return i, j


def move_to_next_button_p2(i, j, line):
    """From i-th row and j-th column of the design keypad, follow instruction line."""
    for char in line:
        if char == "U":
            if i > 0 and DESIGN_KEYPAD[i - 1][j] is not None:
                i -= 1
        elif char == "L":
            if j > 0 and DESIGN_KEYPAD[i][j - 1] is not None:
                j -= 1
        elif char == "D":
            if i < 4 and DESIGN_KEYPAD[i + 1][j] is not None:
                i += 1
        elif char == "R":
            if j < 4 and DESIGN_KEYPAD[i][j + 1] is not None:
                j += 1
    return i, j


if __name__ == "__main__":
    main()

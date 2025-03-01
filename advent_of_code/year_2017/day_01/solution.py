"""Solution --- Day 1: Inverse Captcha ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    captcha_solution = solve_p1(filename)
    print(f"P1: the solution to the part-1 captcha is {captcha_solution}.")
    captcha_solution = solve_p2(filename)
    print(f"P2: the solution to the part-2 captcha is {captcha_solution}.")


def solve_p1(filename):
    """Take the sum of digits matching the next digit in the circular list."""
    digits = tools.read_stripped(__file__, filename)
    captcha_solution = 0
    # Compare with next digit:
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            captcha_solution += int(digits[i])
    # Compare with next digit accounting for circularity:
    if digits[-1] == digits[0]:
        captcha_solution += int(digits[-1])
    return captcha_solution


def solve_p2(filename):
    """Take the sum of digits matching their counterparts in the other half."""
    digits = tools.read_stripped(__file__, filename)
    half_len = len(digits) // 2
    captcha_solution = 0
    # Compare with second half:
    for i in range(half_len):
        if digits[i] == digits[i + half_len]:
            captcha_solution += int(digits[i])
    # Double to account for symmetry:
    return 2 * captcha_solution


if __name__ == "__main__":
    main()

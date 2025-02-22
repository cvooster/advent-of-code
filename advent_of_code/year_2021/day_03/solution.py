"""Solution --- Day 3: Binary Diagnostic ---"""

import operator

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    power_consumption = solve_p1(filename)
    print(f"P1: the submarine's power consumption is {power_consumption}.")
    life_support_rating = solve_p2(filename)
    print(f"P2: the submarine's life support rating is {life_support_rating}.")


def solve_p1(filename):
    """Compute and multiply gamma and epsilon rates for the diagnostic report."""
    lines = tools.read_stripped_lines(__file__, filename)
    counts = [column.count("1") for column in zip(*lines)]
    half_len_report, is_odd = divmod(len(lines), 2)
    if not is_odd and half_len_report in counts:
        raise RuntimeError("Instructions needed to handle ties!")
    # Determine the gamma rate, and flip to get the epsilon rate:
    gamma_rate = int("".join(["1" if c > half_len_report else "0" for c in counts]), 2)
    epsilon_rate = (1 << len(counts)) - 1 - gamma_rate
    return gamma_rate * epsilon_rate


def solve_p2(filename):
    """Compute and multiply the oxygen generator rating and the CO2 scrubber rating."""
    lines = tools.read_stripped_lines(__file__, filename)
    oxygen_rating = compute_rating_multiplicand(lines, True)
    co2_rating = compute_rating_multiplicand(lines, False)
    return oxygen_rating * co2_rating


def compute_rating_multiplicand(candidates, keep_most):
    """Filter on most/least common value in a bit position until one number remains."""
    comparison_operator = operator.ge if keep_most else operator.lt
    bit_position = 0
    try:
        while len(candidates) > 1:
            ones, zeros = [], []
            for num in candidates:
                ones.append(num) if num[bit_position] == "1" else zeros.append(num)
            candidates = ones if comparison_operator(len(ones), len(zeros)) else zeros
            bit_position += 1
    except IndexError as e:
        raise RuntimeError("More than one candidate when the end is reached!") from e
    return int(candidates.pop(), 2)


if __name__ == "__main__":
    main()

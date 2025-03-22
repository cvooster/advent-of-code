"""Solution --- Day 1: Chronal Calibration ---

For part 2, note that the first frequency to be reached twice (if it exists) must be
reached for the first time during the first pass of the list. This could be proved by
contradiction: assuming that the frequency is first reached during the m-th and then the
n-th pass of the list, with 1 < m <= n, one can show that there exists a frequency that
is reached during both the (m-1)th and the (n-1)th pass.
"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    frequency = solve_p1(filename)
    print(f"P1: the changes result in a frequency of {frequency}.")
    frequency = solve_p2(filename)
    print(f"P2: the first frequency reached twice is {frequency}.")


def solve_p1(filename):
    """Sum all frequency changes to obtain the resulting frequency."""
    return sum([int(x) for x in tools.read_stripped_lines(__file__, filename)])


def solve_p2(filename):
    """Process list (repeatedly), and determine first frequency to be reached twice."""
    changes = [int(x) for x in tools.read_stripped_lines(__file__, filename)]
    frequency, seen = 0, {0}
    for change in changes:
        frequency += change
        if frequency in seen:
            return frequency
        seen.add(frequency)
    return repeat_processing(frequency, changes, seen)


def repeat_processing(frequency, changes, seen):
    """Repeat list processing until an already reached frequency is revisited."""
    ub = get_maximum_nr_repetitions(seen, frequency)
    for _ in range(ub):
        for change in changes:
            frequency += change
            if frequency in seen:
                return frequency
    raise RuntimeError("No frequency is reached twice!")


def get_maximum_nr_repetitions(seen, change_per_pass):
    """Get an upper bound on the required number of repetitions."""
    if change_per_pass == 0:
        raise ValueError("No repetition should be needed if cumulative change is zero!")
    return (max(seen) - min(seen)) // abs(change_per_pass)


if __name__ == "__main__":
    main()

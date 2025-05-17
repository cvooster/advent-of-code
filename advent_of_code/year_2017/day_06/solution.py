"""Solution --- Day 6: Memory Reallocation ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    cycle_nr = solve_p1(filename)
    print(f"P1: cycle {cycle_nr} is the first to produce an already visited state.")
    nr_cycles = solve_p2(filename)
    print(f"P2: it takes {nr_cycles} cycles to revisit an already visited state.")


def solve_p1(filename):
    """Determine the first cycle to produce an already visited state."""
    cycle_nr, _ = run_reallocation(filename)
    return cycle_nr


def solve_p2(filename):
    """Determine the number of cycles it takes to revisit an already visited state."""
    cycle_nr, previous_cycle_nr = run_reallocation(filename)
    return cycle_nr - previous_cycle_nr


def run_reallocation(filename):
    """Run the reallocation routine until an already visited state is reached."""
    banks = [int(x) for x in tools.read_stripped(__file__, filename).split()]
    cache = {}
    nr_banks = len(banks)
    cycle_nr = 0
    while True:
        banks_tuple = tuple(banks)
        if banks_tuple in cache:
            return cycle_nr, cache[banks_tuple]
        cache[banks_tuple] = cycle_nr
        perform_redistribution_cycle(banks, nr_banks)
        cycle_nr += 1


def perform_redistribution_cycle(banks, nr_banks):
    """Remove all blocks from the bank with the most blocks, and redistribute."""
    max_blocks = max(banks)
    idx = banks.index(max_blocks)
    banks[idx] = 0
    for j in range(idx + 1, idx + 1 + max_blocks):
        banks[j % nr_banks] += 1


if __name__ == "__main__":
    main()

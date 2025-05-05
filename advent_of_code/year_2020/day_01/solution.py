"""Solution --- Day 1: Report Repair ---"""

from advent_of_code.commons import tools

REQUIRED_SUM = 2020


def main():
    filename = "input.txt"
    expense_multiple = solve_p1(filename)
    print(f"P1: the two entries multiply to {expense_multiple}.")
    expense_multiple = solve_p2(filename)
    print(f"P2: the three entries multiply to {expense_multiple}.")


def solve_p1(filename):
    """Find two expenses with the required sum, and multiply."""
    return multiply_expenses(filename, 2)


def solve_p2(filename):
    """Find three expenses with the required sum, and multiply."""
    return multiply_expenses(filename, 3)


def multiply_expenses(filename, nr_entries):
    """Find (first) nr_entries expenses with required sum, and multiply."""
    expenses = sorted(int(x) for x in tools.read_stripped_lines(__file__, filename))

    def search_product(remaining, nr_entries, idx):
        """Return product of nr_entries after `idx` summing to `remaining` or None."""
        if nr_entries == 1:
            return remaining if remaining in expenses[idx:] else None

        # Because expenses have been sorted, one can bound entries to branch on:
        upper_bound = remaining / nr_entries
        for idx_ in range(idx, len(expenses)):
            entry = expenses[idx_]
            if entry > upper_bound:
                break
            product = search_product(remaining - entry, nr_entries - 1, idx_ + 1)
            if product is not None:
                return product * entry
        return None

    expense_multiple = search_product(REQUIRED_SUM, nr_entries, 0)
    if expense_multiple is None:
        raise RuntimeError("No valid combination of expenses found!")
    return expense_multiple


if __name__ == "__main__":
    main()

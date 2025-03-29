"""Solution --- Day 4: High-Entropy Passphrases ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_valid = solve_p1(filename)
    print(f"P1: under the original rules, {nr_valid} passphrases are valid.")
    nr_valid = solve_p2(filename)
    print(f"P2: under the new rules, {nr_valid} passphrases are valid.")


def solve_p1(filename):
    """Count the number of valid passphrases under the original rules."""
    return count_valid_passphrases(filename, is_valid_p1)


def solve_p2(filename):
    """Count the number of valid passphrases under the new rules."""
    return count_valid_passphrases(filename, is_valid_p2)


def count_valid_passphrases(filename, is_valid):
    """Count the number of valid passphrases, as per the `is_valid` function."""
    passphrases = tools.read_stripped_lines(__file__, filename)
    return sum([is_valid(p) for p in passphrases])


def is_valid_p1(passphrase):
    """Check whether the passphrase contains no duplicate words."""
    words = passphrase.split()
    return len(words) == len(set(words))


def is_valid_p2(passphrase):
    """Check whether the passphrase contains no two words that are anagrams."""
    sorted_words = [tuple(sorted(word)) for word in passphrase.split()]
    return len(sorted_words) == len(set(sorted_words))


if __name__ == "__main__":
    main()

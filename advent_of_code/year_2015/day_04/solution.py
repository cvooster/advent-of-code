"""Solution --- Day 4: The Ideal Stocking Stuffer ---"""

import hashlib

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    lowest_valid = solve_p1(filename)
    print(f"P1: {lowest_valid} is the lowest to produce a hash starting with 5 zeroes.")
    lowest_valid = solve_p2(filename)
    print(f"P2: {lowest_valid} is the lowest to produce a hash starting with 6 zeroes.")


def solve_p1(filename):
    """Find the lowest number to produce a hash starting with 5 zeroes."""
    secret_key = tools.read_stripped(__file__, filename)
    return find_lowest_number(secret_key, "0" * 5)


def solve_p2(filename):
    """Find the lowest number to produce a hash starting with 6 zeroes."""
    secret_key = tools.read_stripped(__file__, filename)
    return find_lowest_number(secret_key, "0" * 6)


def find_lowest_number(key, start):
    """Find the lowest positive number to produce an MD5 hash with the given start.

    In order to determine digests of data sharing a common initial substring, namely the
    key, initialize a hash object by feeding the (encoded) substring. Then use copies of
    this object to be updated with candidate positive numbers.
    """
    init_md5_object = hashlib.md5(key.encode())
    number = 1
    while True:
        md5_object = init_md5_object.copy()
        md5_object.update(str(number).encode())
        if md5_object.hexdigest().startswith(start):
            break
        number += 1
    return number


if __name__ == "__main__":
    main()

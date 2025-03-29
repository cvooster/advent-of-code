"""Solution --- Day 5: How About a Nice Game of Chess? ---"""

import hashlib

from advent_of_code.commons import tools

PASSWORD_LEN = 8


def main():
    filename = "input.txt"
    password = solve_p1(filename)
    print(f"P1: the password of the first door is {password}.")
    password = solve_p2(filename)
    print(f"P2: the password of the second door is {password}.")


def solve_p1(filename):
    """Crack the password of the first security door."""
    md5_hash_iter = set_up_hash_iterator(filename)
    return "".join([next(md5_hash_iter)[5] for _ in range(PASSWORD_LEN)])


def solve_p2(filename):
    """Crack the password of the second security door."""
    md5_hash_iter = set_up_hash_iterator(filename)
    password = [None] * PASSWORD_LEN
    while any(char is None for char in password):
        md5_hash = next(md5_hash_iter)
        position = int(md5_hash[5], 16)
        if position < PASSWORD_LEN and password[position] is None:
            password[position] = md5_hash[6]
    return "".join(password)


def set_up_hash_iterator(filename):
    """Read file input, and set up an iterator over MD5 hashes starting with 5 zeros."""
    door_id = tools.read_stripped(__file__, filename)
    init_md5_object = hashlib.md5(door_id.encode())
    return generate_hash(init_md5_object, "0" * 5)


def generate_hash(init_md5_object, start):
    """Generate MD5 hashes by updating an initial object with an increasing index."""
    index = 0
    while True:
        md5_object = init_md5_object.copy()
        md5_object.update(str(index).encode())
        md5_hash = md5_object.hexdigest()
        if md5_hash.startswith(start):
            yield md5_hash
        index += 1


if __name__ == "__main__":
    main()

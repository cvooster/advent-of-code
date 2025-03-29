"""Solution --- Day 4: Security Through Obscurity ---

The name of the room where the North Pole objects are stored, defined as a constant in
this solution, is not specified in the problem description. Instead, it was inferred by
manually inspecting all decrypted names for the retrieved puzzle input.
"""

from collections import Counter

from advent_of_code.commons import tools

STORAGE_ROOM_NAME = "northpole object storage"


def main():
    filename = "input.txt"
    sector_id_sum = solve_p1(filename)
    print(f"P1: the sector IDs of real rooms sum to {sector_id_sum}.")
    sector_id = solve_p2(filename)
    print(f"P2: the objects are stored in a room with sector ID {sector_id}.")


def solve_p1(filename):
    """Identify rooms that are real, and sum their sector IDs."""
    return sum([sector_id for _, sector_id in identify_real_rooms(filename)])


def solve_p2(filename):
    """Identify the sector ID of the room in which the objects are stored."""
    for encrypted_name, sector_id in identify_real_rooms(filename):
        if decrypt(encrypted_name, sector_id) == STORAGE_ROOM_NAME:
            return sector_id
    raise RuntimeError("No storage room could be identified!")


def identify_real_rooms(filename):
    """Generate the encrypted name and sector ID for all real rooms."""
    lines = tools.read_stripped_lines(__file__, filename)
    for line in lines:
        encrypted_name, rest = line.rsplit("-", maxsplit=1)
        sector_id, checksum = int(rest[:-7]), rest[-6:-1]
        if find_most_common_letters(encrypted_name) == checksum:
            yield (encrypted_name, sector_id)


def find_most_common_letters(encrypted_name):
    """Order the five most common letters, breaking ties by alphabetization."""
    c = Counter(encrypted_name.replace("-", ""))
    most_common = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    return "".join([char for char, _ in most_common[:5]])


def decrypt(encrypted_name, sector_id):
    """Decrypt a name that has been encrypted with a shift cipher."""
    shift = sector_id % 26
    return "".join([" " if c == "-" else rotate(c, shift) for c in encrypted_name])


def rotate(letter, shift):
    """Rotate the letter by a given right shift."""
    return chr((ord(letter) - 97 + shift) % 26 + 97)


if __name__ == "__main__":
    main()

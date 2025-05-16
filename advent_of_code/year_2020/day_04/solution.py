"""Solution --- Day 4: Passport Processing ---"""

import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    nr_valid = solve_p1(filename)
    print(f"P1: all required fields are present in {nr_valid} passports.")
    nr_valid = solve_p2(filename)
    print(f"P2: all required fields have valid values in {nr_valid} passports.")


def solve_p1(filename):
    """Count the number of passports with all required fields."""
    return count_valid_passports(filename, is_valid_p1)


def solve_p2(filename):
    """Count the number of passports with valid values at all required fields."""
    return count_valid_passports(filename, is_valid_p2)


def count_valid_passports(filename, is_valid):
    """Count the number of valid passwords as per the `is_valid` function."""
    passports = tools.read_stripped(__file__, filename).split("\n\n")
    return sum([is_valid(passport) for passport in passports])


def is_valid_p1(passport):
    """Check whether the given passport has all required fields."""
    fields = {pair.split(":")[0] for ln in passport.split("\n") for pair in ln.split()}
    return fields.issuperset(VALIDATION_MAP)


def is_valid_p2(passport):
    """Check whether the given passport has all required fields with valid values."""
    fields = set()
    for ln in passport.split("\n"):
        for pair in ln.split():
            key, val = pair.split(":")
            if not is_valid_field_value(key, val):
                return False
            fields.add(key)
    return fields.issuperset(VALIDATION_MAP)


def is_valid_field_value(key, val):
    """Check whether `val` is a valid value for field `key`."""
    return VALIDATION_MAP[key](val) if key in VALIDATION_MAP else True


def is_valid_byr(val):
    """Check whether `val` is a valid value for field byr."""
    return val.isdecimal() and 1920 <= int(val) <= 2002


def is_valid_iyr(val):
    """Check whether `val` is a valid value for field iyr."""
    return val.isdecimal() and 2010 <= int(val) <= 2020


def is_valid_eyr(val):
    """Check whether `val` is a valid value for field eyr."""
    return val.isdecimal() and 2020 <= int(val) <= 2030


def is_valid_hgt(val):
    """Check whether `val` is a valid value for field hgt."""
    if val.endswith("in"):
        return val[:-2].isdecimal() and 59 <= int(val[:-2]) <= 76
    if val.endswith("cm"):
        return val[:-2].isdecimal() and 150 <= int(val[:-2]) <= 193
    return False


def is_valid_hcl(val):
    """Check whether `val` is a valid value for field hcl."""
    return len(val) == 7 and val[0] == "#" and re.fullmatch(r"[0-9a-f]*", val[1:])


def is_valid_ecl(val):
    """Check whether `val` is a valid value for field ecl."""
    return val in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def is_valid_pid(val):
    """Check whether `val` is a valid value for field pid."""
    return len(val) == 9 and val.isdecimal()


VALIDATION_MAP = {
    "byr": is_valid_byr,
    "iyr": is_valid_iyr,
    "eyr": is_valid_eyr,
    "hgt": is_valid_hgt,
    "hcl": is_valid_hcl,
    "ecl": is_valid_ecl,
    "pid": is_valid_pid,
}


if __name__ == "__main__":
    main()

"""This module provides useful tools for solving Advent of Code puzzles."""

from pathlib import Path


def read_stripped_lines(pathname, filename):
    """Process file, and return content as a list of strings without trailing spaces."""
    with Path(pathname).with_name(filename).open() as file_object:
        file_lines = [line.rstrip() for line in file_object]
        if not file_lines:
            raise OSError("The input file is empty!")
    return file_lines


def read_lines(pathname, filename):
    """Process file, and return content as a list of strings with trailing spaces."""
    with Path(pathname).with_name(filename).open() as file_object:
        file_lines = [line for line in file_object]
        if not file_lines:
            raise OSError("The input file is empty!")
    return file_lines


def read_stripped(pathname, filename):
    """Process file, and return content as a string without trailing spaces."""
    with Path(pathname).with_name(filename).open() as file_object:
        file_string = file_object.read().rstrip()
        if not file_string:
            raise OSError("The input file is empty!")
    return file_string

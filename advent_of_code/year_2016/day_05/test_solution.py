import unittest

import advent_of_code.year_2016.day_05.solution as s05

FILENAME = "input.txt"
FILENAME_EXAMPLE = "input_example.txt"


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2016-05."""

    def test_example_part_1(self):
        """Test whether part 1 outcome for the example is as expected."""
        actual = s05.solve_p1(FILENAME_EXAMPLE)
        self.assertEqual(actual, "18f47a30")

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s05.solve_p1(FILENAME)
        self.assertEqual(actual, "1a3099aa")

    def test_example_part_2(self):
        """Test whether part 2 outcome for the example is as expected."""
        actual = s05.solve_p2(FILENAME_EXAMPLE)
        self.assertEqual(actual, "05ace8e3")

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s05.solve_p2(FILENAME)
        self.assertEqual(actual, "694190cd")


if __name__ == "__main__":
    unittest.main()

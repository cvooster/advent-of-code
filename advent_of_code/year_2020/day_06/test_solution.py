import unittest

import advent_of_code.year_2020.day_06.solution as s06

FILENAME = "input.txt"
FILENAME_EXAMPLE = "input_example.txt"


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2020-06."""

    def test_example_part_1(self):
        """Test whether part 1 outcome for the example is as expected."""
        actual = s06.solve_p1(FILENAME_EXAMPLE)
        self.assertEqual(actual, 11)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s06.solve_p1(FILENAME)
        self.assertEqual(actual, 6911)

    def test_example_part_2(self):
        """Test whether part 2 outcome for the example is as expected."""
        actual = s06.solve_p2(FILENAME_EXAMPLE)
        self.assertEqual(actual, 6)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s06.solve_p2(FILENAME)
        self.assertEqual(actual, 3473)


if __name__ == "__main__":
    unittest.main()

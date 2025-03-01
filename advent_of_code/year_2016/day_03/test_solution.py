import unittest

import advent_of_code.year_2016.day_03.solution as s03

FILENAME = "input.txt"


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2016-03."""

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s03.solve_p1(FILENAME)
        self.assertEqual(actual, 982)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s03.solve_p2(FILENAME)
        self.assertEqual(actual, 1826)


if __name__ == "__main__":
    unittest.main()

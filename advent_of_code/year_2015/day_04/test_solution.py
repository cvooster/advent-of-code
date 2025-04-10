import unittest

import advent_of_code.year_2015.day_04.solution as s04

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(2))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2015-04."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (609043, 1048970)
        for filename, expected in zip(FILENAMES_EXAMPLES, expecteds):
            with self.subTest(filename=filename):
                actual = s04.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s04.solve_p1(FILENAME)
        self.assertEqual(actual, 346386)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s04.solve_p2(FILENAME)
        self.assertEqual(actual, 9958218)


if __name__ == "__main__":
    unittest.main()

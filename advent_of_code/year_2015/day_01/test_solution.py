import unittest

import advent_of_code.year_2015.day_01.solution as s01

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(11))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2015-01."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (0, 0, 3, 3, 3, -1, -1, -3, -3)
        for filename, expected in zip(FILENAMES_EXAMPLES[:9], expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s01.solve_p1(FILENAME)
        self.assertEqual(actual, 74)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (1, 5)
        for filename, expected in zip(FILENAMES_EXAMPLES[9:], expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s01.solve_p2(FILENAME)
        self.assertEqual(actual, 1795)


if __name__ == "__main__":
    unittest.main()

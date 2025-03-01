import unittest

import advent_of_code.year_2017.day_01.solution as s01

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(9))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2017-01."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (3, 4, 0, 9)
        for filename, expected in zip(FILENAMES_EXAMPLES[:4], expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s01.solve_p1(FILENAME)
        self.assertEqual(actual, 1341)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (6, 0, 4, 12, 4)
        for filename, expected in zip(FILENAMES_EXAMPLES[4:], expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s01.solve_p2(FILENAME)
        self.assertEqual(actual, 1348)


if __name__ == "__main__":
    unittest.main()

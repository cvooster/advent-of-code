import unittest

import advent_of_code.year_2017.day_03.solution as s03

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(4))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2017-03."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (0, 3, 2, 31)
        for filename, expected in zip(FILENAMES_EXAMPLES, expecteds):
            with self.subTest(filename=filename):
                actual = s03.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s03.solve_p1(FILENAME)
        self.assertEqual(actual, 480)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (2, 23, 25)
        for filename, expected in zip(FILENAMES_EXAMPLES[:3], expecteds):
            with self.subTest(filename=filename):
                actual = s03.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s03.solve_p2(FILENAME)
        self.assertEqual(actual, 349975)


if __name__ == "__main__":
    unittest.main()

import unittest

import advent_of_code.year_2019.day_03.solution as s03

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(3))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2019-03."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (6, 159, 135)
        for filename, expected in zip(FILENAMES_EXAMPLES, expecteds):
            with self.subTest(filename=filename):
                actual = s03.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s03.solve_p1(FILENAME)
        self.assertEqual(actual, 1225)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (30, 610, 410)
        for filename, expected in zip(FILENAMES_EXAMPLES, expecteds):
            with self.subTest(filename=filename):
                actual = s03.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s03.solve_p2(FILENAME)
        self.assertEqual(actual, 107036)


if __name__ == "__main__":
    unittest.main()

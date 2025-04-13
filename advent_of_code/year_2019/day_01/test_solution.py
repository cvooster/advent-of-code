import unittest

import advent_of_code.year_2019.day_01.solution as s01

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(4))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2019-01."""

    def test_example_part_1(self):
        """Test whether part 1 outcomes for the examples are as expected."""
        expecteds = (2, 2, 654, 33583)
        for filename, expected in zip(FILENAMES_EXAMPLES, expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p1(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s01.solve_p1(FILENAME)
        self.assertEqual(actual, 3437969)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (2, 966, 50346)
        for filename, expected in zip(FILENAMES_EXAMPLES[1:], expecteds):
            with self.subTest(filename=filename):
                actual = s01.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s01.solve_p2(FILENAME)
        self.assertEqual(actual, 5154075)


if __name__ == "__main__":
    unittest.main()

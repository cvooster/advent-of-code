import unittest

import advent_of_code.year_2020.day_04.solution as s04

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(3))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2020-04."""

    def test_example_part_1(self):
        """Test whether part 1 outcome for the example is as expected."""
        actual = s04.solve_p1(FILENAMES_EXAMPLES[0])
        self.assertEqual(actual, 2)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s04.solve_p1(FILENAME)
        self.assertEqual(actual, 190)

    def test_example_part_2(self):
        """Test whether part 2 outcomes for the examples are as expected."""
        expecteds = (0, 4)
        for filename, expected in zip(FILENAMES_EXAMPLES[1:], expecteds):
            with self.subTest(filename=filename):
                actual = s04.solve_p2(filename)
                self.assertEqual(actual, expected)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s04.solve_p2(FILENAME)
        self.assertEqual(actual, 121)


if __name__ == "__main__":
    unittest.main()

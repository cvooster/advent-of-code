import unittest

import advent_of_code.year_2015.day_05.solution as s05

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(2))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2015-05."""

    def test_example_part_1(self):
        """Test whether part 1 outcome for the example is as expected."""
        actual = s05.solve_p1(FILENAMES_EXAMPLES[0])
        self.assertEqual(actual, 2)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s05.solve_p1(FILENAME)
        self.assertEqual(actual, 258)

    def test_example_part_2(self):
        """Test whether part 2 outcome for the example is as expected."""
        actual = s05.solve_p2(FILENAMES_EXAMPLES[1])
        self.assertEqual(actual, 2)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s05.solve_p2(FILENAME)
        self.assertEqual(actual, 53)


if __name__ == "__main__":
    unittest.main()

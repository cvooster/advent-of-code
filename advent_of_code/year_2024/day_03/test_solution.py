import unittest

import advent_of_code.year_2024.day_03.solution as s03

FILENAME = "input.txt"
FILENAMES_EXAMPLES = tuple(f"input_example_{i+1}.txt" for i in range(2))


class TestSolution(unittest.TestCase):
    """Tests for the solution of puzzle 2024-03."""

    def test_example_part_1(self):
        """Test whether part 1 outcome for the example is as expected."""
        actual = s03.solve_p1(FILENAMES_EXAMPLES[0])
        self.assertEqual(actual, 161)

    def test_aoc_verified_part_1(self):
        """Test whether part 1 outcome is as verified by AoC."""
        actual = s03.solve_p1(FILENAME)
        self.assertEqual(actual, 161289189)

    def test_example_part_2(self):
        """Test whether part 2 outcome for the example is as expected."""
        actual = s03.solve_p2(FILENAMES_EXAMPLES[1])
        self.assertEqual(actual, 48)

    def test_aoc_verified_part_2(self):
        """Test whether part 2 outcome is as verified by AoC."""
        actual = s03.solve_p2(FILENAME)
        self.assertEqual(actual, 83595109)


if __name__ == "__main__":
    unittest.main()

"""Solution --- Day 2: Rock Paper Scissors ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    total_score = solve_p1(filename)
    print(f"P1: the part-1 score following the strategy guide is {total_score}.")
    total_score = solve_p2(filename)
    print(f"P2: the part-2 score following the strategy guide is {total_score}.")


def solve_p1(filename):
    """Determine the part-1 total score of following the strategy guide."""
    return evaluate_strategy_guide(filename, construct_score_map_p1())


def solve_p2(filename):
    """Determine the part-2 total score of following the strategy guide."""
    return evaluate_strategy_guide(filename, construct_score_map_p2())


def evaluate_strategy_guide(filename, score_map):
    """Read file input, and calculate the total score of the strategy guide."""
    round_lines = tools.read_stripped_lines(__file__, filename)
    return sum(score_map[line] for line in round_lines)


def construct_score_map_p1():
    """Map all possible rounds to a score, with X/Y/Z interpreted as shapes."""
    shape_score = {"X": 1, "Y": 2, "Z": 3}
    # fmt: off
    outcome_map = {
        "A X": "D", "A Y": "W", "A Z": "L",
        "B X": "L", "B Y": "D", "B Z": "W",
        "C X": "W", "C Y": "L", "C Z": "D",
    }
    # fmt: on
    outcome_score = {"W": 6, "D": 3, "L": 0}
    return {k: shape_score[k[2]] + outcome_score[v] for k, v in outcome_map.items()}


def construct_score_map_p2():
    """Map all possible rounds to a score, with X/Y/Z interpreted as outcomes."""
    outcome_score = {"X": 0, "Y": 3, "Z": 6}
    # fmt: off
    shape_map = {
        "A X": "S", "A Y": "R", "A Z": "P",
        "B X": "R", "B Y": "P", "B Z": "S",
        "C X": "P", "C Y": "S", "C Z": "R",
    }
    # fmt: on
    shape_score = {"R": 1, "P": 2, "S": 3}
    return {k: shape_score[v] + outcome_score[k[2]] for k, v in shape_map.items()}


if __name__ == "__main__":
    main()

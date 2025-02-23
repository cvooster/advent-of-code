"""Solution --- Day 4: Giant Squid ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    final_score = solve_p1(filename)
    print(f"P1: the first winning board's final score is {final_score}.")
    final_score = solve_p2(filename)
    print(f"P2: the last winning board's final score is {final_score}.")


def solve_p1(filename):
    """Simulate bingo until the first board wins, and compute that board's score."""
    boards, draws = initialize_bingo(filename)
    for draw in draws:
        draw_number(boards, draw)
        winners, _ = seperate_winners(boards)
        if winners:
            return get_single_winner(winners).unmarked_sum * draw
    raise RuntimeError("All numbers have been drawn, but no board has won!")


def solve_p2(filename):
    """Simulate bingo until the last board wins, and compute that board's score."""
    active_boards, draws = initialize_bingo(filename)
    for draw in draws:
        draw_number(active_boards, draw)
        winners, active_boards = seperate_winners(active_boards)
        if not active_boards:
            return get_single_winner(winners).unmarked_sum * draw
    raise ValueError("All numbers have been drawn, but not all boards have won!")


def initialize_bingo(filename):
    """Read file input, and set the bingo boards and the sequence of drawn numbers."""
    draws_line, *groups = tools.read_stripped(__file__, filename).split("\n\n")
    draws = [int(x) for x in draws_line.split(",")]
    boards = []
    for group in groups:
        grid = [[int(x) for x in line.split()] for line in group.split("\n")]
        boards.append(Board(grid))
    return boards, draws


def draw_number(boards, draw):
    """Mark the drawn number on all bingo boards."""
    for board in boards:
        board.mark_drawn_number(draw)


def seperate_winners(boards):
    """Determine which boards have won and which boards have not (are ongoing)."""
    winners = [b for b in boards if b.has_won]
    active_boards = [b for b in boards if not b.has_won]
    return winners, active_boards


def get_single_winner(winners):
    """Return the only element of `winners`, and raise an error in case of a tie."""
    if len(winners) > 1:
        raise RuntimeError("There is a tie between winners!")
    return winners[0]


class Board:
    """Class to represent a bingo board consisting of a 5x5 grid of numbers."""

    ROWS = 5
    COLS = 5

    def __init__(self, grid):
        """Create a map from numbers to positions, and initialize statistics."""
        self.number_map = self._create_map(grid)
        self.unmarked_sum = sum(self.number_map.keys())
        self.nr_unmarked_by_row = [self.COLS] * self.ROWS
        self.nr_unmarked_by_col = [self.ROWS] * self.COLS
        self.has_won = False

    def _create_map(self, grid):
        """Transform the grid to a map from numbers to their row and column."""
        return {grid[i][j]: (i, j) for i in range(self.ROWS) for j in range(self.COLS)}

    def mark_drawn_number(self, draw):
        """Update statistics if the drawn number is on the board."""
        if draw in self.number_map:
            i, j = self.number_map[draw]
            self.unmarked_sum -= draw
            self.nr_unmarked_by_row[i] -= 1
            self.nr_unmarked_by_col[j] -= 1
            if self.nr_unmarked_by_row[i] == 0 or self.nr_unmarked_by_col[j] == 0:
                self.has_won = True


if __name__ == "__main__":
    main()

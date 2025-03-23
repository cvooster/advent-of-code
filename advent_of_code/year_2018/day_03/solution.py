"""Solution --- Day 3: No Matter How You Slice It ---

This solution uses a generalized form of the inclusion-exclusion principle to compute
the answer to part 1. However, given the input file, and the number of overlaps and the
size of the entire piece of fabric, a solution that explicitly stores the coordinates
of all squares in a set would not only have been simpler but probably also faster.
"""

from collections import defaultdict
import re

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    total_area = solve_p1(filename)
    print(f"P1: {total_area} square inches of fabric are within multiple claims.")
    non_overlapping_id = solve_p2(filename)
    print(f"P2: the claim with ID {non_overlapping_id} does not overlap.")


def solve_p1(filename):
    r"""Determine the total area covered by two or more claims.

    This computation proceeds by computing n-wise intersections for all n. The areas of
    these intersections can be combined into a total area using the following identity:
    \sum_{j=2}^{n} (-1)^{j} (j-1) \binom{n}{j} = 1. By this identity, one can count the
    area covered by exactly n claims once, for all n >= 2, by once adding the area of
    pairwise intersections, twice subtracting the area for triple-wise intersections,
    and so on.
    """
    rectangles = initialize_rectangles(filename)
    indices_pairwise = initialize_pairs(rectangles)

    # Track n-wise intersections as rectangles together with the highest claim index
    # (ID minus one) used in the intersection. The index is to break symmetry when
    # generating (n+1)wise intersections:
    n_wise_intersections = [(r, i) for i, r in enumerate(rectangles)]

    def update_intersections(n_wise_intersections):
        """Generate all (n+1)-wise intersections from the n-wise intersections."""
        new_intersections = []
        for rectangle, i in n_wise_intersections:
            for j in indices_pairwise[i]:
                intersection = rectangle.intersect(rectangles[j])
                if intersection:
                    new_intersections.append((intersection, j))
        return new_intersections

    # The following loop has at most len(rectangles) iterations, but terminates early
    # when all n-wise intersections are empty for a given value of n:
    total_area = 0
    sign = 1
    coefficient = 1
    while n_wise_intersections:
        n_wise_intersections = update_intersections(n_wise_intersections)
        area_sum = sum([r.get_area() for r, _ in n_wise_intersections])
        total_area += sign * coefficient * area_sum
        sign *= -1
        coefficient += 1
    return total_area


def solve_p2(filename):
    """Identify the ID of the non-overlapping claim."""
    rectangles = initialize_rectangles(filename)
    for i in range(len(rectangles)):
        if does_intersect_with_none(rectangles, i):
            return i + 1
    raise RuntimeError("All claims overlap with another claim!")


def initialize_rectangles(filename):
    """Read file input, and initialize a list of rectangular claims."""
    lines = tools.read_stripped_lines(__file__, filename)
    regex = re.compile(r"(\d+),(\d+): (\d+)x(\d+)")
    rectangles = []
    for line in lines:
        nums = [int(x) for x in regex.search(line).groups()]
        xmin, xmax = nums[0], nums[0] + nums[2]
        ymin, ymax = nums[1], nums[1] + nums[3]
        rectangles.append(Rectangle(xmin, xmax, ymin, ymax))
    return rectangles


def initialize_pairs(rectangles):
    """Construct a dictionary with indices of pairs of intersecting rectangles."""
    indices_pairwise = defaultdict(list)
    for i in range(len(rectangles)):
        # Consider only i and j such that i < j in order to break symmetry:
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].does_intersect(rectangles[j]):
                indices_pairwise[i].append(j)
    return indices_pairwise


def does_intersect_with_none(rectangles, i):
    """Determine if the i-th rectangle intersects with no other rectangle."""
    for j in range(len(rectangles)):
        if i != j and rectangles[i].does_intersect(rectangles[j]):
            return False
    return True


class Rectangle:
    """Class to represent rectangles of fabric."""

    def __init__(self, xmin, xmax, ymin, ymax):
        """Set min (inclusive) and max (exclusive) distances from top left corner."""
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def does_intersect(self, other):
        """Check whether this rectangle intersects with another rectangle."""
        return (
            self.xmin < other.xmax
            and other.xmin < self.xmax
            and self.ymin < other.ymax
            and other.ymin < self.ymax
        )

    def intersect(self, other):
        """Return the intersection of this rectangle with another rectangle or None."""
        if self.does_intersect(other):
            xmin = max(self.xmin, other.xmin)
            xmax = min(self.xmax, other.xmax)
            ymin = max(self.ymin, other.ymin)
            ymax = min(self.ymax, other.ymax)
            return Rectangle(xmin, xmax, ymin, ymax)

    def get_area(self):
        """Return the number of squares covered by this rectangle."""
        return (self.xmax - self.xmin) * (self.ymax - self.ymin)


if __name__ == "__main__":
    main()

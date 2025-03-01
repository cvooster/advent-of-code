"""Solution --- Day 2: I Was Told There Would Be No Math ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    paper_sum = solve_p1(filename)
    print(f"P1: the elves should order {paper_sum} total square feet of paper.")
    ribbon_sum = solve_p2(filename)
    print(f"P2: the elves should order {ribbon_sum} feet of ribbon.")


def solve_p1(filename):
    """Compute the total amount of wrapping paper to be ordered."""
    return sum_resource_requirement(filename, compute_wrapping_paper)


def solve_p2(filename):
    """Compute the total amount of ribbon to be ordered."""
    return sum_resource_requirement(filename, compute_ribbon)


def sum_resource_requirement(filename, compute_requirement):
    """Use `compute_requirement` to compute the total amount for a resource."""
    lines = tools.read_stripped_lines(__file__, filename)
    edges_list = [[int(x) for x in line.split("x")] for line in lines]
    return sum([compute_requirement(*edges) for edges in edges_list])


def compute_wrapping_paper(length, width, height):
    """Compute wrapping paper requirement for a present of the given dimensions."""
    faces = [length * width, length * height, width * height]
    return 2 * sum(faces) + min(faces)


def compute_ribbon(length, width, height):
    """Compute ribbon requirement for a present of the given dimensions."""
    volume = length * width * height
    return 2 * (length + width + height - max(length, width, height)) + volume


if __name__ == "__main__":
    main()

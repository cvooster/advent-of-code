"""Solution --- Day 1: The Tyranny of the Rocket Equation ---"""

from advent_of_code.commons import tools


def main():
    filename = "input.txt"
    fuel_sum = solve_p1(filename)
    print(f"P1: without the mass of added fuel, the total requirement is {fuel_sum}.")
    fuel_sum = solve_p2(filename)
    print(f"P2: with the mass of added fuel, the total requirement is {fuel_sum}.")


def solve_p1(filename):
    """Sum the fuel required to launch the modules based on mass excluding fuel."""
    masses = [int(x) for x in tools.read_stripped_lines(__file__, filename)]
    return sum([compute_fuel_p1(m) for m in masses])


def solve_p2(filename):
    """Sum the fuel required to launch the modules based on mass including fuel."""
    masses = [int(x) for x in tools.read_stripped_lines(__file__, filename)]
    return sum([compute_fuel_p2(m) for m in masses])


def compute_fuel_p1(mass):
    """Compute the fuel required for the given module mass."""
    return mass // 3 - 2


def compute_fuel_p2(mass):
    """Compute the fuel required for the given module mass and the added fuel."""
    total = 0
    fuel = compute_fuel_p1(mass)
    while fuel > 0:
        total += fuel
        fuel = compute_fuel_p1(fuel)
    return total


if __name__ == "__main__":
    main()

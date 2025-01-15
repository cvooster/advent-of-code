[![Badge Python](https://img.shields.io/badge/python-3.13-green)](https://www.python.org/)
[![Badge Flake8](https://img.shields.io/badge/flake8-checked-orange)](https://flake8.pycqa.org/en/latest/)
[![Badge Black](https://img.shields.io/badge/code%20style-black-black)](https://black.readthedocs.io/en/stable/)

# [Advent of Code](https://adventofcode.com/)

This repository contains my solutions to puzzles from Advent of Code. For more
information about this programming puzzle event, which has run every December since
2015, see [https://adventofcode.com/about](https://adventofcode.com/about). Having been
introduced to these puzzles in 2023, I decided to compete for time in
[2023 and 2024](#rankings), and also solve the puzzles from earlier editions.

## :information_source: About the Solutions

All solutions in this repository have been developed using Python, and tested using
Python version 3.13.0. The code on the *main* branch does not depend on any third-party
packages. Note that I have modified the solutions compared with their versions at the
time of answer submission. In some cases, these modifications have been inspired by
ideas from others.

## :rocket: Instructions

```tree
advent_of_code
└── advent_of_code
    ├── commons
    │   ├── __init__.py
    │   ├── tools.py
    ├── year_2015
    │   ├── day_01
    │   │   ├── __init__.py
    │   │   ├── solution.py
    │   │   └── test_solution.py
    │   ├── ...
    ├── ...
```

### Inputs

For every year and day, there is a folder with a script `solution.py` to solve both
parts of the puzzle. However, the `input.txt` file with puzzle input is omitted from
this public repository. In order to run the script, a file with (any user's) input must
be added to the folder. Successfully running the test script `test_solution.py` requires
this file to contain *my* input, and an `input_example.txt` file (or multiple such
files, distinguished by a numeric suffix) to contain the example input that comes with
the problem description.

### Installation

The solution scripts may import functionality from the `commons` folder. The recommended
way to make these imports work is to install this project as a package. Documentation is
available at [https://pip.pypa.io/en/stable/topics/local-project-installs/](https://pip.pypa.io/en/stable/topics/local-project-installs/). 

### Development

Install the optional dependencies, and run `pre-commit install`. This sets up a Git
pre-commit hook that checks whether changes align with the project's code style before
accepting a commit.

## :bar_chart: Rankings

To see how my speed would compare to other participants, I started my December mornings
in 2023 and 2024 at 6:00 AM working on the puzzles at the time of their release. Both
years, there was exactly one part of a day where I ended up on the global leaderboard
for the 100 fastest solves. The full results (ranks) are listed below:

| Day         | Part 1 | &nbsp; &nbsp; &nbsp; | Part 2 | &nbsp; &nbsp; &nbsp; | Day         | Part 1 | &nbsp; &nbsp; &nbsp; | Part 2 | &nbsp; &nbsp; &nbsp; |
| :---------: | -----: | :----------------------: | -----: | :----------------------: | :---------: | -----: | :----------------------: | -----: | :----------------------: |
| **2023-25** | 3368   |        | 2792   |  | **2024-25** | 288    |        | 240    |  |
| **2023-24** | 992    |        | 2741   |  | **2024-24** | 1443   |        | 2371   |  |
| **2023-23** | 1501   |        | 2138   |  | **2024-23** | 1121   |        | 1030   |  |
| **2023-22** | 62     | :star: | 640    |  | **2024-22** | 327    |        | 1650   |  |
| **2023-21** | 108    |        | 4392   |  | **2024-21** | 1607   |        | 2476   |  |
| **2023-20** | 1607   |        | 550    |  | **2024-20** | 99     | :star: | 3486   |  |
| **2023-19** | 2253   |        | 1780   |  | **2024-19** | 403    |        | 394    |  |
| **2023-18** | 1238   |        | 5554   |  | **2024-18** | 316    |        | 194    |  |
| **2023-17** | 810    |        | 682    |  | **2024-17** | 2469   |        | 3806   |  |
| **2023-16** | 358    |        | 1251   |  | **2024-16** | 622    |        | 1421   |  |
| **2023-15** | 1999   |        | 2101   |  | **2024-15** | 824    |        | 3486   |  |
| **2023-14** | 3223   |        | 1027   |  | **2024-14** | 2112   |        | 1581   |  |
| **2023-13** | 2734   |        | 1525   |  | **2024-13** | 2234   |        | 4403   |  |
| **2023-12** | 2590   |        | 1440   |  | **2024-12** | 3519   |        | 1087   |  |
| **2023-11** | 122    |        | 207    |  | **2024-11** | 412    |        | 1552   |  |
| **2023-10** | 1010   |        | 1659   |  | **2024-10** | 860    |        | 1082   |  |
| **2023-09** | 819    |        | 660    |  | **2024-09** | 567    |        | 2675   |  |
| **2023-08** | 678    |        | 2198   |  | **2024-08** | 5126   |        | 3781   |  |
| **2023-07** | 1564   |        | 3029   |  | **2024-07** | 1085   |        | 3680   |  |
| **2023-06** | 172    |        | 5463   |  | **2024-06** | 1904   |        | 4731   |  |
| **2023-05** | 2590   |        | 1870   |  | **2024-05** | 2371   |        | 856    |  |
| **2023-04** | 198    |        | 159    |  | **2024-04** | 3025   |        | 1775   |  |
| **2023-03** | 379    |        | 301    |  | **2024-03** | 786    |        | 399    |  |
| **2023-02** | 612    |        | 1448   |  | **2024-02** | 797    |        | 572    |  |
| **2023-01** | 633    |        | 310    |  | **2024-01** | 579    |        | 297    |  |

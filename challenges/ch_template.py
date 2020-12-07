from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
import re
from functools import reduce
from collections import Counter

# Parameters
DAY, YEAR = 1, 2020


# Part 1
def part1(raw_data):
    return 0


# Part 2
def part2(raw_data):
    return 0


def main():
    # Fetch data and pre-process
    raw_data = get_raw(DAY, YEAR)

    # TODO manually comment part1/part2 until auto submit in place
    # Fill result and uncomment assert once result is validated

    # Part1
    res = part1(raw_data)
    # assert (res == 0)
    print(f"Ch{DAY}.1:", res)

    # Part2
    res = part2(raw_data)
    # assert (res == 0)
    print(f"Ch{DAY}.2:", res)


if __name__ == '__main__':
    main()

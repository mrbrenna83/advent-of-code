from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
from functools import reduce
from collections import Counter


# Parameters
DAY, YEAR = 6, 2020


# Part 1
def part1(raw_data):
    """
    Input already a list of groups
    Collpse group, count unique (without \n), then sum up for groups
    """
    res1 = sum([len(Counter(r.replace('\n','')).items()) for r in raw_data])
    return res1


# Part 2
def part2(raw_data):
    """
    Input already a list of groups
    Get a list of unique answer per person, for each gruop
    Intersect all answers per group, then count and sum up
    """
    answers = [[set(Counter(p).keys()) for p in x] for x in [r.split() for r in raw_data]]
    return sum([len(reduce(lambda a,b: a.intersection(b), ans)) for ans in answers])


def main():
    # Fetch data and pre-process
    # Note: Data already list of groups
    raw_data = get_string_group_array(DAY, YEAR)

    # TODO manually comment part1/part2 until auto submit in place
    # Fill result and uncomment assert once result is validated

    # Part1
    res = part1(raw_data)
    print(f"Ch{DAY}.1:", res)

    # Part2
    res = part2(raw_data)
    print(f"Ch{DAY}.2:", res)


if __name__ == '__main__':
    main()

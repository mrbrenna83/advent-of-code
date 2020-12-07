from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
from functools import reduce


# Parameters
DAY, YEAR = 3, 2020


def count_trees(map_data, h_step, v_step):
    """
    On row idx, position is idx*h_step.
    We search position in a modulo map_len map.
    Return True if a tree is found in position
    """
    map_len = len(map_data[0])
    return sum([1 for i, m in enumerate(map_data[::v_step]) if m[(i * h_step) % map_len] == '#'])


# Part 1
def part1(raw_data):
    return count_trees(raw_data, 3, 1)


# Part 2
def part2(raw_data):
    # Horz and Vert steps to analyze
    h_steps = [1, 3, 5, 7, 1]
    v_steps = [1, 1, 1, 1, 2]

    paths_trees = map(lambda h, v: count_trees(raw_data, h, v), h_steps, v_steps)
    res2 = reduce(lambda a, b: a*b, paths_trees, 1)
    return res2


def main():
    # Fetch data and pre-process
    raw_data = get_string_array(DAY, YEAR)

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

from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
from functools import reduce


# Parameters
DAY, YEAR = 5, 2020


def get_sid(raw_pid):
    """
    Transform code into seat ID

    binary tree, 10-digit codes (7:row,3:col)
    row: 'F' lower-half, 'B':higher-half
    col: 'L' lower-half, 'R':higher-half

    Compute only range lower bound (upper bound will converge)
    Lower bound changes only if we select the upper-half ('B', 'R')
    Traverse backwards so that 1<<i is increasing - feel more comfortable ;-)

    """
    high = ['B', 'R']
    sid = sum([1 << i[0] for i in enumerate(raw_pid[-1::-1]) if i[1] in high])
    return sid


# Part 1
def part1(raw_data):
    """
    Get all seat IDs, then max
    """
    sids = list(map(get_sid, raw_data))
    return max(sids)


# Part 2
def part2(raw_data):
    """
    Get all seat IDs.
    Min and max will define existing seat boundaries.
    Given that target seat ID is not on the boundary, then min<id<max holds
    """
    # Get all seat IDs
    sids = list(map(get_sid, raw_data))

    res2 = list(filter(lambda sid: min(sids) < sid < max(sids) and sid not in sids, range(1024)))
    assert(len(res2) == 1)
    return res2[0]


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

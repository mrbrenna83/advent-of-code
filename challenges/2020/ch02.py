from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
import re


# Parameters
DAY, YEAR = 2, 2020


# Part 1
def part1(raw_data):

    res1 = 0
    for r in raw_data:
        m = re.match("([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)", r.strip())
        if m:
            pmin = int(m.group(1))
            pmax = int(m.group(2))
            c = m.group(3)
            p = m.group(4)
            if pmin <= p.count(c) <= pmax:
                res1 += 1

    return res1


# Part 2
def part2(raw_data):
    res2 = 0

    for r in raw_data:
        m = re.match("([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)", r.strip())
        if m:
            p1 = int(m.group(1))
            p2 = int(m.group(2))
            c = m.group(3)
            p = m.group(4)
            if (p[p1-1] == c) and (p[p2-1] != c) \
                or (p[p1-1] != c) and (p[p2-1] == c):
                res2 += 1

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

from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array

# Parameters
DAY, YEAR = 1, 2020


def find_y_tgt(y, tgt, data):
    """
    y[0]: current element idx
    y[1]: current element value

    search a value in data from y[0]+1 to end in data so that sums to
    current y[1] to target value tgt

    next(filter) to return first value (if any, None otherwise)
    """
    return next(filter(lambda z: z == (tgt - y[1]), data[y[0] + 1:]), None) is not None


# Part 1
def part1(data):
    """
    Simplify search given that x+y and y+x is the same.
    Then x in (1:len) and y(x+1:len)
    Try with nested filter
    """
    res1 = next(filter(lambda x: find_y_tgt(x, 2020, data), enumerate(data)), None)
    assert(res1 is not None)
    return res1[1]*(2020-res1[1])


# Part 2
def part2(data):
    """
    Simplify search given that all x,y,z permutation sums the same
    Then x in (1:len) and y(x+1:len) and z in (y+1:len)
    Try with nested filter
    """
    for x in enumerate(data):
        ry = next(filter(lambda y: find_y_tgt(y, 2020 - x[1], data), enumerate(data[1:])), None)
        if ry:
            break

    assert(ry is not None)
    return x[1]*ry[1]*(2020-x[1]-ry[1])


def main():
    # Fetch data and pre-process
    data = get_int_array(DAY, YEAR)

    # TODO manually comment part1/part2 until auto submit in place
    # Fill result and uncomment assert once result is validated

    # Part1
    res = part1(data)
    print(f"Ch{DAY}.1:", res)

    # Part2
    res = part2(data)
    print(f"Ch{DAY}.2:", res)


if __name__ == '__main__':
    main()

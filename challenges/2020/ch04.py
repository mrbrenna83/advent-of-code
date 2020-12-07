from aoc.input import get_raw, get_int_array, get_string_array, get_string_group_array
from functools import reduce
from collections import Counter
import re


# Parameters
DAY, YEAR = 4, 2020


# Checks are kept as simple as possible, just to fit the problem
def check_year(y, min_y, max_y):
    """
    Check if string is a 4-digit year in range
    """
    m = re.match('([0-9]{4})', y)
    return m and min_y <= int(m.group(1)) <= max_y


def check_hgt(h):
    """
    Check height to be a 3digit (cm) or 2digit (in), in valid range
    """
    m = re.match('([0-9]{3})cm', h)
    if m and 150 <= int(m.group(1)) <= 193: return True
    m = re.match('([0-9]{2})in', h)
    return m and 59 <= int(m.group(1)) <= 76


# Other checks are just list search or successful pattern matching
PASSPORT_FIELD_CHECK = {'byr': lambda y: check_year(y, 1920, 2020),
                        'iyr': lambda y: check_year(y, 2010, 2020),
                        'eyr': lambda y: check_year(y, 2020, 2030),
                        'hgt': lambda h: check_hgt(h),
                        'hcl': lambda h: re.match('#([0-9a-z]{6})', h),
                        'ecl': lambda e: e in 'amb blu brn gry grn hzl oth',
                        'pid': lambda p: re.match('^([0-9]{9}$)', p)}


def s2dict(data):
    """
    Convert passport string to dict. Keys and values are string, k:v and space-separated only
    """
    return {d[0]:d[1] for d in [dd.split(':') for dd in data.split()]}


def valid_passport_fields(data):
    """
    Simplified: all passport fields name must be in string
    """
    return sum([1 for k in PASSPORT_FIELD_CHECK if k in data]) == 7


def valid_passport(data):
    """
    Passport fields MUST match all 7 conditions
    """
    data_d = s2dict(data)
    return sum([1 for k, v in data_d.items() if PASSPORT_FIELD_CHECK.get(k, lambda a: False)(v)]) == 7


def part1(raw_data):
    return sum([1 for r in raw_data if valid_passport_fields(r)])


def part2(raw_data):
    return sum([1 for r in raw_data if valid_passport(r)])


def main():
    # Fetch data and pre-process
    # All rows in a group collapsed into a single one, as space-separated string list
    raw_data = [p.replace('\n', ' ') for p in get_string_group_array(DAY, YEAR)]

    # TODO manually comment part1/part2 until auto submit in place
    # Fill result and uncomment assert once result is validated

    # Part 1
    res = part1(raw_data)
    print(f"Ch{DAY}.1:", res)

    # Part 2
    res = part2(raw_data)
    print(f"Ch{DAY}.2:", res)


if __name__ == '__main__':
    main()

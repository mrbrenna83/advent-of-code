# Modules to download problems inputs

from .auth import aoc_cookies
import requests
import os


def fetch_data(day, year):
    """
    Download challenge input from internet
    """
    input_file = f'data/{year}/{day}.dat'
    if not os.path.exists(input_file):
        # Create day folders
        # os.makedirs(f'tests/{year}', exist_ok=True)
        os.makedirs(f'data/{year}', exist_ok=True)

        # uri_text = f"https://adventofcode.com/{year}/day/{day}"
        uri_input = f"https://adventofcode.com/{year}/day/{day}/input"

        auth_cookie = aoc_cookies()
        print(f"Downloading {uri_input} ...")
        r = requests.get(uri_input, cookies=auth_cookie)
        print(f"Saving {input_file} ...")
        open(input_file, "w").write(r.text)

    return input_file


def fetch_tests(day, year, force=False):
    """
    Get tests array in challenge text
    FIXME now Download challenge text from internet
    """
    text_file = f'tests/{year}/{day}.text'
    if os.path.exists(text_file):
        # Create day folders
        os.makedirs(f'tests/{year}', exist_ok=True)
        uri_text = f"https://adventofcode.com/{year}/day/{day}"
        auth_cookie = aoc_cookies()
        print(f"Downloading {uri_text} ...")
        r = requests.get(uri_text, cookies=auth_cookie)
        print(f"Saving {uri_text} ...")
        open(uri_text, "w").write(r.text)

    return text_file


def get_raw(day, year, test_id=None):
    """
    Fetch data, return as raw content.
    """
    input_file = fetch_data(day, year)
    # Strip last CR as raw data is usually passed to split()
    return open(input_file).read().strip()


def get_int_array(day, year, test_id=None):
    """
    Transform raw data into integer array
    """
    return [int(c) for c in get_raw(day, year).split('\n')]


def get_string_array(day, year, test_id=None):
    """
    Transform raw data into string array
    """
    return get_raw(day, year).split('\n')


def get_string_group_array(day, year, test_id=None):
    """
    Transform raw data into line group array (\n\n separator)
    """
    return get_raw(day, year).split('\n\n')

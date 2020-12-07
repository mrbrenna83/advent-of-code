AOC_COOKIES_FILE = "challenges/aoc_cookies.dat"


def aoc_cookies():
    import json
    return json.loads(open(AOC_COOKIES_FILE, 'r').read())


if __name__ == "__main__":
    import json

    # TODO : fill this structure and run this module to save
    _aoc_cookies = {
        "_ga": "(data goes here)",
        "_gid": "(data goes here)",
        "session": "(data goes here)"
    }

    open(AOC_COOKIES_FILE, 'w').write(json.dumps(_aoc_cookies))

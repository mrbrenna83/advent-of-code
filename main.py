from importlib import import_module
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--orig', action='store_true')
    parser.add_argument('--fetch-data', action='store_true')
    parser.add_argument('--fetch-tests', action='store_true')
    parser.add_argument('--year', default=2020, type=int)
    parser.add_argument('day', type=int)

    args = parser.parse_args()

    orig = "_orig" if args.orig else ""
    day = args.day
    year = args.year

    ch = import_module(f"challenges.{year}.ch{day:02d}{orig}")
    ch.main()

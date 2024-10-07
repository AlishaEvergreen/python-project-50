#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli_parser import build_arg_parser


def main():
    first_file, second_file, format = build_arg_parser()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()

import argparse


def build_arg_parser():
    '''Create and configure an argument parser for
    comparing two configuration files.'''
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", default="stylish",
                        help="set format of output",
                        )

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format

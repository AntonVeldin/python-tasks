# tail.py

import os
import argparse

# region parse arguments
arg_parser = argparse.ArgumentParser(prog='tail',
                                     usage='%(prog)s [-f] [-n N] file_name',
                                     description='Hi! This is Anton Veldin\'s tail utility version!',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
arg_parser.add_argument('-n',
                        type=int,
                        action='store',
                        default=-10,
                        help='number of lines: if negative - to tail; if positive - from start')
arg_parser.add_argument('-f',
                        '--follow',
                        action='store_true',
                        help='output appended lines as the file grows')
arg_parser.add_argument('file_name',
                        type=str,
                        action='store',
                        help='text file or path')
args = arg_parser.parse_args()
# endregion parse arguments


class Reader:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_lines(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name) as file:
                return file.readlines()
        else:
            print(f'File "{self.file_name}" didn\'t find.')
            exit()

    def tail(self, n: int):
        """ If n - negative: output n lines from a tail of the text file.
        If n - positive: output all lines start from n.

        If --follow is marked true - output appended data as the file grows."""

        lines = self.read_lines()
        base_count = len(lines)
        print(''.join(lines[n-1:]))

        if args.follow:
            while True:
                lines = self.read_lines()
                count = len(lines)
                if count > base_count:
                    print(''.join(lines[base_count:]))
                    base_count = count


if __name__ == '__main__':
    reader = Reader(args.file_name)
    reader.tail(args.n)

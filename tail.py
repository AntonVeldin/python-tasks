import argparse

# region parse arguments
from datetime import datetime

my_parser = argparse.ArgumentParser(prog='py_tail',
                                    usage='%(prog)s [-f] [n] file_name',
                                    description='Hi! This is Anton Veldin\'s tail utility version!')
my_parser.add_argument('n',
                       type=int,
                       action='store',
                       nargs='?',
                       default=10,
                       help='number of lines to tail (default 10)')
my_parser.add_argument('-f',
                       '--follow',
                       action='store_true',
                       help='output appended data as the file grows')
my_parser.add_argument('file_name',
                       type=str,
                       action='store',
                       help='text file or path')
args = my_parser.parse_args()
# endregion parse arguments


class Reader:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_lines(self):
        with open(self.file_name) as f:
            return f.readlines()

    def tail(self, n):
        """Output n lines from a tail of the text file.
        If follow is true - output appended data as the file grows."""

        lines = self.read_lines()
        base_count = len(lines)
        print(''.join(lines[-n:]))
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

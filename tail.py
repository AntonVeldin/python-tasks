import argparse


# region parse arguments
my_parser = argparse.ArgumentParser(prog='py_tail',
                                    usage='%(prog)s [-f] [n] file_name',
                                    description='Hi! This is Anton Veldin\'s tail utility version!')
my_parser.add_argument('n_lines',
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

    def read_file(self):
        with open(self.file_name) as f:
            lines = f.readlines()
            count_of_lines = len(lines)
            return lines, count_of_lines

    def tail(self, n_lines):
        """Output n lines from a tail of the text file.
        If follow is true - output appended data as the file grows."""

        lines, base_count_of_lines = self.read_file()
        print(''.join(lines[-n_lines:]))
        if args.follow:
            while True:
                lines, count_of_lines = self.read_file()
                if count_of_lines > base_count_of_lines:
                    print(''.join(lines[base_count_of_lines:]))
                    base_count_of_lines = count_of_lines


if __name__ == '__main__':
    reader = Reader(args.file_name)
    reader.tail(args.n_lines)

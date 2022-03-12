import argparse


# region parse arguments
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
                       help='path to text file')
args = my_parser.parse_args()
# endregion parse arguments


class TailReader:

    def __init__(self, n, file_name):
        """
        Arguments:
        n -- number of lines to tail
        file_name -- path to text file"""
        self.file_name = file_name
        self.n = n

    def read(self):
        """Вывод последних n строк текстового файла."""
        def base_read():
            try:
                with open(self.file_name, 'r') as file:
                    lines = file.readlines()
                    return print(''.join(lines[-self.n:]))
            except FileNotFoundError:
                print(f'File "{self.file_name}" didn\'t find.')

        if not args.follow:
            base_read()
        else:
            print('Option "follow" turned on.')
            base_read()


if __name__ == '__main__':
    TailReader(args.n, args.file_name).read()

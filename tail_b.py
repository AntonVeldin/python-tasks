# tail.py

import os
FILE_NAME = 'log.txt'
N_LINES = 10


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

    def tail_b(self, n=10):
        size = os.path.getsize(self.file_name)
        print(f'Size: {size/1048576} mb')
        line_counter = 0

        with open(self.file_name, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while line_counter != n:
                    while file.read(1) != b'\n':
                        file.seek(-2, os.SEEK_CUR)
                        # Get current position of cursor
                        # pos = file.tell()
                        # print(f'Current position: {pos}')
                    line_counter += 1
                    file.seek(-2, os.SEEK_CUR)

            except OSError:
                print(f'2.2')
                file.seek(0)
            last_lines = file.readlines()[1:]
            print(''.join([byte_line.decode() for byte_line in last_lines]))
        return last_lines


if __name__ == '__main__':
    reader = Reader(FILE_NAME)
    line = reader.tail_b(10)

import os.path

N_LINES = 1000000
FILE = 'log.txt'


def create_file(file_name: str):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write('1')
            return True
    return False


def find_last_line(file_name: str):
    with open(file_name, 'r') as file:
        return int(file.readlines()[-1:][0])


def write_lines(file_name: str, lines: int):
    """Add N lines with increment 1"""

    created_file = create_file(file_name)
    if created_file:
        last_line = 1
        lines -= 1
    else:
        last_line = find_last_line(file_name)

    with open(file_name, 'a') as file:
        for i in range(lines):
            last_line += 1
            file.write(f'\n{last_line}')

        return print(f'Last line is {last_line}.')


if __name__ == '__main__':
    write_lines(FILE, N_LINES)

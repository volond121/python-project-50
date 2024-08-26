import argparse
from gendiff.get_json_diff import generate_diff 

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=str)
parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
args = parser.parse_args()

FILE_1 = args.first_file
FILE_2 = args.second_file


def main():
    print(generate_diff(FILE_1, FILE_2))


if __name__ == '__main__':
    main()

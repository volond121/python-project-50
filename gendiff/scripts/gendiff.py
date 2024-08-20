import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', metavar='first_file', type=str)
parser.add_argument('second_file', metavar='second_file', type=set)
args = parser.parse_args()


def main():
    print("Hello!")


if __name__ == '__main__':
    main()

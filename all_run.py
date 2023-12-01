""" Run all Advent of Code 2015 daily puzzles with live input """

from advent import Runner, file_to_string
from day01 import Day01


def main():
    """ stub for main() """
    Runner(Day01(file_to_string("data\\day01.txt"))).run()


if __name__ == '__main__':
    main()

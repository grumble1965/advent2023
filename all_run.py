""" Run all Advent of Code 2015 daily puzzles with live input """

from advent import Runner, file_to_string
from day00 import Day00


def main():
    """ stub for main() """
    Runner(Day00(file_to_string("data\\day00.txt"))).run()


if __name__ == '__main__':
    main()

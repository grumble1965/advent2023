""" Run all Advent of Code 2015 daily puzzles with live input """

from advent import Runner, file_to_string
from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04
from day05 import Day05
from day06 import Day06
from day07 import Day07
from day08 import Day08
from day09 import Day09
from day10 import Day10
from day11 import Day11
from day12 import Day12
from day13 import Day13


def main():
    """ stub for main() """
    Runner(Day01(file_to_string("data\\day01.txt"))).run()
    Runner(Day02(file_to_string("data\\day02.txt"))).run()
    Runner(Day03(file_to_string("data\\day03.txt"))).run()
    Runner(Day04(file_to_string("data\\day04.txt"))).run()
    Runner(Day05(file_to_string("data\\day05.txt"))).run()
    Runner(Day06(file_to_string("data\\day06.txt"))).run()
    Runner(Day07(file_to_string("data\\day07.txt"))).run()
    Runner(Day08(file_to_string("data\\day08.txt"))).run()
    Runner(Day09(file_to_string("data\\day09.txt"))).run()
    Runner(Day10(file_to_string("data\\day10.txt"))).run()
    Runner(Day11(file_to_string("data\\day11.txt"))).run()
    Runner(Day12(file_to_string("data\\day12.txt"))).run()
    Runner(Day13(file_to_string("data\\day13.txt"))).run()


if __name__ == '__main__':
    main()

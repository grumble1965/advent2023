""" Code to unit test Advent of Code 2015 solutions """

import unittest
from day01 import Day01
from day02 import Day02


class Day01Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        day = Day01([
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet'])
        day.parse()
        self.assertEqual(142, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day01([
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',])
        day.parse()
        self.assertEqual(281, day.part_two())


class Day02Tests(unittest.TestCase):
    """ day 2 tests """

    def test_part_one(self):
        """ part one """
        day = Day02(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'])
        day.parse()
        self.assertEqual(8, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day02(['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'])
        day.parse()
        self.assertEqual(281, day.part_two())


if __name__ == '__main__':
    unittest.main()

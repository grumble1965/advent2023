""" Code to unit test Advent of Code 2015 solutions """

import unittest
from day01 import Day01


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
        """ part one """
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


if __name__ == '__main__':
    unittest.main()

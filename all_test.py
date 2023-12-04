""" Code to unit test Advent of Code 2015 solutions """

import unittest
from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04

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
        self.assertEqual(2286, day.part_two())


class Day03Tests(unittest.TestCase):
    """ day 3 tests """

    def test_part_one(self):
        """ part one """
        day = Day03([
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..'
        ])
        day.parse()
        self.assertEqual(4361, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day03([
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..'
        ])
        day.parse()
        self.assertEqual(467835, day.part_two())

class Day04Tests(unittest.TestCase):
    """ day 4 tests """

    def test_part_one(self):
        """ part one """
        day = Day04([
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11])'])
        day.parse()
        self.assertEqual(13, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day04([
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11])'])
        day.parse()
        self.assertEqual(30, day.part_two())

if __name__ == '__main__':
    unittest.main()

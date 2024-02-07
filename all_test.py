""" Code to unit test Advent of Code 2015 solutions """

import unittest
from advent import file_to_string
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
from day14 import Day14
from day15 import Day15
from day16 import Day16
from day17 import Day17
from day18 import Day18
from day19 import Day19
from day20 import Day20
from day21 import Day21
from day22 import Day22
from day23 import Day23
from day24 import Day24

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
            '7pqrstsixteen', ])
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


class Day05Tests(unittest.TestCase):
    """ day 5 tests """

    def test_part_one(self):
        """ part one """
        input_text = file_to_string("data\\day05-test.txt")
        day = Day05(input_text)
        day.parse()
        self.assertEqual(35, day.part_one())

    def test_part_two(self):
        """ part two """
        input_text = file_to_string("data\\day05-test.txt")
        day = Day05(input_text)
        day.parse()
        self.assertEqual(46, day.part_two())


class Day06Tests(unittest.TestCase):
    """ day 6 tests """

    def test_part_one(self):
        """ part one """
        input_text = ['Time:      7  15   30',
                      'Distance:  9  40  200']
        day = Day06(input_text)
        day.parse()
        self.assertEqual(288, day.part_one())

    def test_part_two(self):
        """ part two """
        input_text = ['Time:      7  15   30',
                      'Distance:  9  40  200']
        day = Day06(input_text)
        day.parse()
        self.assertEqual(71503, day.part_two())


class Day07Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        day = Day07([
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'])
        day.parse()
        self.assertEqual(6440, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day07([
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'])
        day.parse()
        self.assertEqual(5905, day.part_two())


class Day08Tests(unittest.TestCase):
    """ day 8 tests """

    def test_part_one(self):
        input_one = ['RL',
                     '',
                     'AAA = (BBB, CCC)',
                     'BBB = (DDD, EEE)',
                     'CCC = (ZZZ, GGG)',
                     'DDD = (DDD, DDD)',
                     'EEE = (EEE, EEE)',
                     'GGG = (GGG, GGG)',
                     'ZZZ = (ZZZ, ZZZ)']

        input_two = [
            'LLR',
            '',
            'AAA = (BBB, BBB)',
            'BBB = (AAA, ZZZ)',
            'ZZZ = (ZZZ, ZZZ)'
        ]

        """ part one """
        day = Day08(input_one)
        day.parse()
        self.assertEqual(2, day.part_one())

        day = Day08(input_two)
        day.parse()
        self.assertEqual(6, day.part_one())

    def test_part_two(self):
        """ part two """
        input_three = [
            'LR',
            '',
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)'
        ]

        day = Day08(input_three)
        day.parse()
        self.assertEqual(6, day.part_two())


class Day09Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        day = Day09([
            '0 3 6 9 12 15',
            '1 3 6 10 15 21',
            '10 13 16 21 30 45'])
        day.parse()
        self.assertEqual(114, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day09([
            '0 3 6 9 12 15',
            '1 3 6 10 15 21',
            '10 13 16 21 30 45'])
        day.parse()
        self.assertEqual(2, day.part_two())


class Day10Tests(unittest.TestCase):
    """ day 10 tests """

    def test_part_one(self):
        """ part one """
        day = Day10([
            '.....',
            '.S-7.',
            '.|.|.',
            '.L-J.',
            '.....'])
        day.parse()
        self.assertEqual(4, day.part_one())

        day = Day10([
            '..F7.',
            '.FJ|.',
            'SJ.L7',
            '|F--J',
            'LJ...'])
        day.parse()
        self.assertEqual(8, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day10(['...........',
                     '.S-------7.',
                     '.|F-----7|.',
                     '.||.....||.',
                     '.||.....||.',
                     '.|L-7.F-J|.',
                     '.|..|.|..|.',
                     '.L--J.L--J.',
                     '...........'])
        day.parse()
        day.part_one()
        self.assertEqual(4, day.part_two())

        day = Day10(['.F----7F7F7F7F-7....',
                     '.|F--7||||||||FJ....',
                     '.||.FJ||||||||L7....',
                     'FJL7L7LJLJ||LJ.L-7..',
                     'L--J.L7...LJS7F-7L7.',
                     '....F-J..F7FJ|L7L7L7',
                     '....L7.F7||L7|.L7L7|',
                     '.....|FJLJ|FJ|F7|.LJ',
                     '....FJL-7.||.||||...',
                     '....L---J.LJ.LJLJ...'])
        day.parse()
        day.part_one()
        self.assertEqual(8, day.part_two())

        day = Day10([
            'FF7FSF7F7F7F7F7F---7',
            'L|LJ||||||||||||F--J',
            'FL-7LJLJ||||||LJL-77',
            'F--JF--7||LJLJIF7FJ-',
            'L---JF-JLJIIIIFJLJJ7',
            '|F|F-JF---7IIIL7L|7|',
            '|FFJF7L7F-JF7IIL---7',
            '7-L-JL7||F7|L7F-7F7|',
            'L.L7LFJ|||||FJL7||LJ',
            'L7JLJL-JLJLJL--JLJ.L'])
        day.parse()
        day.part_one()
        self.assertEqual(10, day.part_two())


class Day11Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        day = Day11([
            '...#......',
            '.......#..',
            '#.........',
            '..........',
            '......#...',
            '.#........',
            '.........#',
            '..........',
            '.......#..',
            '#...#.....'])
        day.parse()
        self.assertEqual(374, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day11([
            '...#......',
            '.......#..',
            '#.........',
            '..........',
            '......#...',
            '.#........',
            '.........#',
            '..........',
            '.......#..',
            '#...#.....'])
        day.parse()
        day.factor = 10
        self.assertEqual(1030, day.part_two())

        day.factor = 100
        self.assertEqual(8410, day.part_two())


class Day12Tests(unittest.TestCase):
    """ day 12 tests """

    def test_part_one(self):
        """ part one """
        day = Day12([
            '???.### 1,1,3',
            '.??..??...?##. 1,1,3',
            '?#?#?#?#?#?#?#? 1,3,1,6',
            '????.#...#... 4,1,1',
            '????.######..#####. 1,6,5',
            '?###???????? 3,2,1'])
        day.parse()
        self.assertEqual(21, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day12([
            '???.### 1,1,3',
            '.??..??...?##. 1,1,3',
            '?#?#?#?#?#?#?#? 1,3,1,6',
            '????.#...#... 4,1,1',
            '????.######..#####. 1,6,5',
            '?###???????? 3,2,1'])
        day.parse()
        self.assertEqual(525152, day.part_two())

class Day13Tests(unittest.TestCase):
    """ day 1 tests """

    def test_part_one(self):
        """ part one """
        day = Day13([
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
            '',
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#'])
        day.parse()
        self.assertEqual(2, len(day.grids))

        self.assertEqual( 5, day.find_reflections(day.grids[0].cols))
        self.assertEqual( None, day.find_reflections(day.grids[0].rows))
        self.assertEqual( None, day.find_reflections(day.grids[1].cols))
        self.assertEqual( 4, day.find_reflections(day.grids[1].rows))
        self.assertEqual(405, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day13([
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.',
            '',
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#'])
        day.parse()

        self.assertEqual( None, day.find_smudged_reflections(day.grids[0].cols))
        self.assertEqual( 3, day.find_smudged_reflections(day.grids[0].rows))
        self.assertEqual( None, day.find_smudged_reflections(day.grids[1].cols))
        self.assertEqual( 1, day.find_smudged_reflections(day.grids[1].rows))
        self.assertEqual(400, day.part_two())

class Day14Tests(unittest.TestCase):
    """ day 14 tests """

    def test_part_one(self):
        """ part one """
        day = Day14([
            'O....#....',
            'O.OO#....#',
            '.....##...',
            'OO.#O....O',
            '.O.....O#.',
            'O.#..O.#.#',
            '..O..#O..O',
            '.......O..',
            '#....###..',
            '#OO..#....'])
        day.parse()
        self.assertEqual(136, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day14([
            'O....#....',
            'O.OO#....#',
            '.....##...',
            'OO.#O....O',
            '.O.....O#.',
            'O.#..O.#.#',
            '..O..#O..O',
            '.......O..',
            '#....###..',
            '#OO..#....'])
        day.parse()
        self.assertEqual(64, day.part_two())

class Day15Tests(unittest.TestCase):
    """ day 15 tests """

    def test_part_one(self):
        """ part one """
        self.assertEqual(52, Day15.hash_alg('HASH'))

        day = Day15(['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'])
        day.parse()
        self.assertEqual(1320, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day15(['rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'])
        day.parse()
        self.assertEqual(145, day.part_two())

class Day16Tests(unittest.TestCase):
    """ day 16 tests """

    def test_part_one(self):
        """ part one """
        day = Day16(['.|...\....',
                     '|.-.\.....',
                     '.....|-...',
                     '........|.',
                     '..........',
                     '.........\\',
                     '..../.\\\\..',
                     '.-.-/..|..',
                     '.|....-|.\\',
                     '..//.|....'])
        day.parse()
        self.assertEqual(46, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day16(['.|...\....',
                     '|.-.\.....',
                     '.....|-...',
                     '........|.',
                     '..........',
                     '.........\\',
                     '..../.\\\\..',
                     '.-.-/..|..',
                     '.|....-|.\\',
                     '..//.|....'])
        day.parse()
        self.assertEqual(51, day.part_two())

class Day17Tests(unittest.TestCase):
    """ day 17 tests """

    def test_part_one(self):
        """ part one """
        day = Day17([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day17([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day18Tests(unittest.TestCase):
    """ day 18 tests """

    def test_part_one(self):
        """ part one """
        day = Day18([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day18([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day19Tests(unittest.TestCase):
    """ day 19 tests """

    def test_part_one(self):
        """ part one """
        day = Day19([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day19([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day20Tests(unittest.TestCase):
    """ day 20 tests """

    def test_part_one(self):
        """ part one """
        day = Day20([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day20([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day21Tests(unittest.TestCase):
    """ day 21 tests """

    def test_part_one(self):
        """ part one """
        day = Day21([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day21([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day22Tests(unittest.TestCase):
    """ day 22 tests """

    def test_part_one(self):
        """ part one """
        day = Day22([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day22([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day23Tests(unittest.TestCase):
    """ day 23 tests """

    def test_part_one(self):
        """ part one """
        day = Day23([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day23([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class Day24Tests(unittest.TestCase):
    """ day 24 tests """

    def test_part_one(self):
        """ part one """
        day = Day24([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day24([])
        day.parse()
        # self.assertEqual(-999, day.part_two())

class DayXXTests(unittest.TestCase):
    """ day XX tests """

    def test_part_one(self):
        """ part one """
        day = Day01([])
        day.parse()
        # self.assertEqual(-999, day.part_one())

    def test_part_two(self):
        """ part two """
        day = Day01([])
        day.parse()
        # self.assertEqual(-999, day.part_two())


if __name__ == '__main__':
    unittest.main()

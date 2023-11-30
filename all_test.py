""" Code to unit test Advent of Code 2015 solutions """

import unittest
from day00 import Day00


class Day00Tests(unittest.TestCase):
    """ day 0 tests """

    def test_part_one(self):
        """ part one """
        day = Day00("data\\day00.txt")
        day.parse()
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

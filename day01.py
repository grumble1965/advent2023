""" Day 1 setup """

from advent import Advent, Runner, file_to_string


class Day01(Advent):
    """ Day 1 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.name = "1"
        self.line = input_text
        self.table = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5),
                      ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9),
                      ('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4),
                      ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9)]

    def parse(self):
        pass

    def part_one(self):
        calibration = 0
        for line in self.line:
            idx = 0
            while idx < len(line):
                if line[idx].isdigit():
                    first_digit = ord(line[idx]) - ord('0')
                    break
                idx += 1

            idx = len(line) - 1
            while idx >= 0:
                if line[idx].isdigit():
                    last_digit = ord(line[idx]) - ord('0')
                    break
                idx -= 1

            calibration += (first_digit * 10) + last_digit
        print(f"Calibration total = {calibration}")
        return calibration

    def find_first_match(self, line):
        """return a list of the first occurences of each item in table"""
        matches = []
        for (word, digit) in self.table:
            pos = line.find(word)
            if pos > -1:
                matches.append([digit, word, pos])
        return matches

    def find_last_match(self, line):
        """return a list of the last occurences of each item in table"""
        matches = []
        for (word, digit) in self.table:
            pos = line.rfind(word)
            if pos > -1:
                matches.append([digit, word, pos])
        return matches

    def part_two(self):
        calibration = 0
        for line in self.line:
            first = min(self.find_first_match(line), key=lambda ff: ff[2])
            last = max(self.find_last_match(line), key=lambda ff: ff[2])
            this_line = (first[0] * 10) + last[0]
            # print(f"Cal Line: {this_line}")
            calibration += this_line
        print(f"Calibration total = {calibration}")
        return calibration


def main():
    """ stub for main() """
    aoc1 = Day01(file_to_string("data\\day01.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()

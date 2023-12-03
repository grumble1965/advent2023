""" Day 3 setup """

from advent import Advent, Runner, file_to_string


class Day03(Advent):
    """ Day 3 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "3"
        self.all_numbers = []
        self.part_numbers = []
        self.possible_gears = {}    # dict from (line,idx) -> [number]

    def is_symbol(self, s):
        """ check if a string of length 1 is a symbol """
        if s.isdigit() or s == '.':
            return False
        elif s in ['<', '>', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '/', '=']:
            return True
        else:
            print(f"Unknown symbol: {s}")

    def get_adjacent_chars(self, line_number, left_idx, right_idx):
        """ return a list of the chars that surround a number """
        chars = []
        if line_number - 1 >= 0:
            idx = max(0, left_idx)
            while idx < len(self.input_lines[line_number - 1]) and idx <= right_idx:
                chars.append(
                    (self.input_lines[line_number - 1][idx], line_number - 1, idx))
                idx += 1
        idx = max(0, left_idx)
        while idx < len(self.input_lines[line_number]) and idx <= right_idx:
            chars.append(
                (self.input_lines[line_number][idx], line_number, idx))
            idx += 1
        if line_number + 1 < len(self.input_lines):
            idx = max(0, left_idx)
            while idx < len(self.input_lines[line_number + 1]) and idx <= right_idx:
                chars.append(
                    (self.input_lines[line_number + 1][idx], line_number + 1, idx))
                idx += 1
        return chars

    def parse(self):
        line_num = 0
        while line_num < len(self.input_lines):
            line = self.input_lines[line_num]
            idx = 0
            while idx < len(line):
                if line[idx].isdigit():
                    start = idx
                    idx += 1
                    number = None
                    while idx < len(line) and line[idx].isdigit():
                        idx += 1
                    if idx >= len(line):
                        number = int(line[start:])
                    else:
                        number = int(line[start:idx])

                    self.all_numbers.append(number)

                    # check for an adjacent symbol
                    left_idx = start - 1
                    right_idx = idx

                    adj_chars_tuples = self.get_adjacent_chars(
                        line_num, left_idx, right_idx)

                    if any(self.is_symbol(t) for t, i, j in adj_chars_tuples):
                        self.part_numbers.append(number)

                    for ch, i, j in adj_chars_tuples:
                        if ch == '*':
                            if (i, j) in self.possible_gears:
                                self.possible_gears[(i, j)].append(number)
                            else:
                                self.possible_gears[(i, j)] = [number]

                else:
                    idx += 1
            line_num += 1

    def part_one(self):
        sum_of_part_numbers = sum(self.part_numbers)
        # print(f"{self.all_numbers}")
        # print(f"{self.part_numbers}")
        print(f"Sum of part numbers = {sum_of_part_numbers}")
        return sum_of_part_numbers

    def part_two(self):
        sum_gear_ratios = 0
        for _, number_list in self.possible_gears.items():
            if len(number_list) == 2:
                sum_gear_ratios += number_list[0] * number_list[1]
        print(f"Sum of gear ratios = {sum_gear_ratios}")
        return sum_gear_ratios


def main():
    """ stub for main() """
    aoc3 = Day03(file_to_string("data\\day03.txt"))
    runner = Runner(aoc3)
    runner.run()


if __name__ == '__main__':
    main()

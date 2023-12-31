""" Day 11 setup """

from advent import Advent, Runner, file_to_string
from itertools import combinations

class Day11(Advent):
    """ Day 11 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "11"
        self.factor = 1000000
        self.rows = None
        self.cols = None
        self.stars = []
        self.empty_rows = []
        self.empty_cols = []

    def parse(self):
        self.rows = len(self.input_lines)
        self.cols = len(self.input_lines[0])

        for row_idx in range(self.rows):
            line = self.input_lines[row_idx]
            gals = [col_idx for col_idx in range(self.cols) if line[col_idx] == '#']
            if len(gals) == 0:
                self.empty_rows.append(row_idx)
            else:
                for c in gals:
                    self.stars.append((row_idx, c))

        for col_idx in range(self.cols):
            stars_in_column = [(r,c) for (r,c) in self.stars if col_idx == c]
            if len(stars_in_column) == 0:
                self.empty_cols.append(col_idx)

    def part_one(self):
        paths = []
        for (gal_a, gal_b) in combinations(self.stars, 2):
            a_r, a_c = gal_a
            b_r, b_c = gal_b
            r1, r2 = min(a_r, b_r), max(a_r, b_r)
            c1, c2 = min(a_c, b_c), max(a_c, b_c)
            double_rows = [r for r in range(r1, r2 + 1) if r in self.empty_rows]
            double_cols = [c for c in range(c1, c2 + 1) if c in self.empty_cols]
            distance = abs(a_r - b_r) + abs(a_c - b_c) + len(double_rows) + len(double_cols)
            paths.append(distance)

        sum_of_paths = sum(paths)
        print(f"sum of paths: {sum_of_paths}")
        return sum_of_paths

    def part_two(self):
        factor = self.factor
        paths = []
        for (gal_a, gal_b) in combinations(self.stars, 2):
            a_r, a_c = gal_a
            b_r, b_c = gal_b
            r1, r2 = min(a_r, b_r), max(a_r, b_r)
            c1, c2 = min(a_c, b_c), max(a_c, b_c)
            double_rows = [r for r in range(r1, r2 + 1) if r in self.empty_rows]
            double_cols = [c for c in range(c1, c2 + 1) if c in self.empty_cols]
            distance = abs(a_r - b_r) + abs(a_c - b_c) + ((factor - 1) * len(double_rows)) + ((factor - 1) * len(double_cols))
            paths.append(distance)

        sum_of_paths = sum(paths)
        print(f"sum of paths: {sum_of_paths}")
        return sum_of_paths


def main():
    """ stub for main() """
    aoc11 = Day11(file_to_string("data\\day11.txt"))
    runner = Runner(aoc11)
    runner.run()


if __name__ == '__main__':
    main()

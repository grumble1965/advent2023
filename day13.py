""" Day 13 setup """

from advent import Advent, Runner, file_to_string

class Grid:
    def __init__(self):
        self.rows = []
        self.cols = []

    def add_row(self, new_row):
        self.rows.append(new_row)
        if len(self.cols) == 0:
            for x in new_row:
                self.cols.append([])
        for idx in range(len(new_row)):
            self.cols[idx].append(new_row[idx])

    def finalize(self):
        string_array = []
        for col_array in self.cols:
            col_string = "".join(list(col_array))
            string_array.append(col_string)
        self.cols = string_array

class Day13(Advent):
    """ Day 13 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "13"
        self.grids = []

    def parse(self):
        grid = Grid()
        for line in self.input_lines:
            if line == '':
                grid.finalize()
                if len(grid.rows) + len(grid.cols) > 0:
                    self.grids.append(grid)
                grid = Grid()
            else:
                grid.add_row(line)
        grid.finalize()
        if len(grid.rows) + len(grid.cols) > 0:
            self.grids.append(grid)
        print(f"read {len(self.grids)} grids")

    @staticmethod
    def find_reflections(a) -> int | None:
        matches = set()
        for start in range(1, len(a)):
            count = min(start, len(a)-start)
            refl = True
            for idx in range(0, count):
                left = start - 1 - idx
                right = start + idx
                if not a[left] == a[right]:
                    refl = False
                    break
            if refl:
                matches.add(start)
        if len(matches) != 1:
            return None
        else:
            return matches.pop()

    def part_one(self):
        rows, cols = 0, 0
        for g in self.grids:
            col_ref = self.find_reflections(g.cols)
            if col_ref:
                cols += col_ref
            row_ref = self.find_reflections(g.rows)
            if row_ref:
                rows += row_ref
        summary = 100 * rows + cols
        print(f"Summary = {summary}")
        return summary

    @staticmethod
    def find_smudged_reflections(a) -> int | None:
        matches = set()
        for start in range(1, len(a)):
            count = min(start, len(a)-start)
            diff_count = 0
            for idx in range(0, count):
                left = start - 1 - idx
                right = start + idx
                if a[left] == a[right]:
                    pass
                else:
                    diff_count += len( [idx for idx in range(len(a[left])) if a[left][idx] != a[right][idx]] )
                    if diff_count > 1:
                        break
            if diff_count == 1:
                matches.add(start)
        if len(matches) == 0 or len(matches) > 2:
            return None
        foo = Day13.find_reflections(a)
        if foo is not None and foo in matches:
            matches.remove(foo)
        if len(matches) != 1:
            return None
        else:
            return matches.pop()


    def part_two(self):
        rows, cols = 0, 0
        for g in self.grids:
            col_ref = self.find_smudged_reflections(g.cols)
            if col_ref:
                cols += col_ref
            row_ref = self.find_smudged_reflections(g.rows)
            if row_ref:
                rows += row_ref
        summary = 100 * rows + cols
        print(f"Summary = {summary}")
        return summary


def main():
    """ stub for main() """
    aoc13 = Day13(file_to_string("data\\day13.txt"))
    runner = Runner(aoc13)
    runner.run()


if __name__ == '__main__':
    main()

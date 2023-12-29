""" Day 10 setup """

from advent import Advent, Runner, file_to_string
import math
import re

deltas = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    '.': []
}

class Day10(Advent):
    """ Day 10 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "10"
        self.start = None
        self.rows = None
        self.cols = None
        self.loops = None

    def parse(self):
        self.rows = len(self.input_lines)
        self.cols = len(self.input_lines[0])

        for row in range(len(self.input_lines)):
            if 'S' in self.input_lines[row]:
                self.start = (row, self.input_lines[row].index('S'))
                break

    def get_neighbors(self, row, col):
        ch = self.input_lines[row][col]
        neighbors = []
        for dr, dc in deltas[ch]:
            if 0 <= row+dr < self.rows and 0 <= col + dc <= self.cols:
                nr, nc = row + dr, col + dc
                # make sure that anything we point to can point back to us
                valid = False
                new_ch = self.input_lines[row + dr][col + dc]
                for ndr, ndc in deltas[new_ch]:
                    if nr + ndr == row and nc + ndc == col:
                        valid = True
                        break
                if valid:
                    neighbors.append((nr,nc))
        return neighbors


    def part_one(self):
        # check around start for possible paths
        loop_paths = []
        row_start, col_start = self.start
        for current_row, current_col in self.get_neighbors(row_start, col_start):
            path = [self.start]
            while True:
                nns = self.get_neighbors(current_row, current_col)
                if len(nns) == 1:
                    print(f"Dead end at ({current_row},{current_col})")
                    break
                if len(nns) > 2:
                    print(f"Too many paths at ({current_row},{current_col})")
                    for n in nns:
                        print(f"    {n}")
                    break

                if nns[0] == path[-1]:
                    next_step = nns[1]
                elif nns[1] == path[-1]:
                    next_step = nns[0]
                else:
                    print("Neither neighbor was the last step!")
                    break

                if next_step == path[0]:
                    # print("completed the loop!")
                    path.append((current_row,current_col))
                    loop_paths.append(path)
                    break
                else:
                    path.append((current_row,current_col))
                    current_row, current_col = next_step

        self.loops = loop_paths
        max_loop = max( map(lambda ll: len(ll), loop_paths) )
        max_steps = math.ceil(max_loop / 2)
        print(f"Maximum steps in loop is {max_loop}, yielding {max_steps}")
        return max_steps

    def part_two(self):
        pattern_crossing = re.compile('(L-*7|F-*J)')
        pattern_not_crossing = re.compile('(L-*J|F-*7)')

        if not self.loops:
            raise Exception("No loops - please run part 1")
        loop = self.loops[0]

        # get bounding box
        max_col, max_row, min_col, min_row = self.get_bounding_box(loop)
        # print(f"Box from ({min_row},{min_col}) to ({max_row},{max_col})")

        # for line in self.input_lines:
        #     print(line)

        inside_count = 0
        loop_set = set(loop)
        for r in range(min_row, max_row+1):
            for c in range(min_col, max_col+1):
                if (r,c) in loop_set:
                    inside_count += 0
                else:
                    path_copy = ''
                    for cidx in range(len(self.input_lines[r])):
                        if (r, cidx) not in loop_set:
                            path_copy += '.'
                        else:
                            path_copy += self.input_lines[r][cidx]
                    step_one = pattern_crossing.sub('|', path_copy[min_col:c])
                    step_two = pattern_not_crossing.sub('', step_one)
                    crossings = step_two.count('|')
                    if crossings % 2 == 1 and 'S' not in step_two:
                        inside_count += 1

        print(f"Loop encloses {inside_count} points")
        return inside_count

    def get_bounding_box(self, loop):
        loop_rows = [r for (r, _) in loop]
        loop_cols = [c for (_, c) in loop]
        row_set = set(loop_rows)
        col_set = set(loop_cols)
        min_row = min(row_set)
        min_col = min(col_set)
        max_row = max(row_set)
        max_col = max(col_set)
        return max_col, max_row, min_col, min_row


def main():
    """ stub for main() """
    aoc10 = Day10(file_to_string("data\\day10.txt"))
    runner = Runner(aoc10)
    runner.run()


if __name__ == '__main__':
    main()

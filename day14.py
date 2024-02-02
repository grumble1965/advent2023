""" Day 14 setup """

from advent import Advent, Runner, file_to_string


class Day14(Advent):
    """ Day 14 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.name = "14"
        self.input_lines = input_text
        self.grid = []

    def parse(self):
        for line in self.input_lines:
            self.grid.append(list(line))
        # for row in range(len(self.grid)):
        #     for col in range(len(self.grid[0])):
        #         print(f"{self.grid[row][col]} ", end='')
        #     print()

    def tip_north(self):
        for c in range(len(self.grid[0])):
            column = "".join([self.grid[r][c] for r in range(len(self.grid))])
            while column.find(".O") > -1:
                st = column.find(".O")
                new_col = column[:st] + "O." + column[st+2:]
                column = new_col
            for r in range(len(column)):
                self.grid[r][c] = column[r]

    def tip_south(self):
        for c in range(len(self.grid[0])):
            column = "".join([self.grid[r][c] for r in range(len(self.grid))])
            while column.find("O.") > -1:
                st = column.find("O.")
                new_col = column[:st] + ".O" + column[st+2:]
                column = new_col
            for r in range(len(column)):
                self.grid[r][c] = column[r]

    def tip_east(self):
        for r in range(len(self.grid)):
            row = "".join([self.grid[r][c] for c in range(len(self.grid[r]))])
            while row.find("O.") > -1:
                st = row.find("O.")
                new_row = row[:st] + ".O" + row[st+2:]
                row = new_row
            for c in range(len(row)):
                self.grid[r][c] = row[c]

    def tip_west(self):
        for r in range(len(self.grid)):
            row = "".join([self.grid[r][c] for c in range(len(self.grid[r]))])
            while row.find(".O") > -1:
                st = row.find(".O")
                new_row = row[:st] + "O." + row[st+2:]
                row = new_row
            for c in range(len(row)):
                self.grid[r][c] = row[c]

    def tip_cycle(self):
        self.tip_north()
        self.tip_west()
        self.tip_south()
        self.tip_east()

    def calculate_load_north(self):
        load = 0
        for row_idx in range(len(self.grid)):
            row = self.grid[row_idx]
            load += (row.count('O')) * (len(self.grid) - row_idx)
        return load

    def part_one(self):
        self.tip_north()
        # print('tipping north')
        # for row in range(len(self.grid)):
        #     for col in range(len(self.grid[0])):
        #         print(f"{self.grid[row][col]} ", end='')
        #     print()
        load = self.calculate_load_north()
        print(f"Total north load = {load}")
        return load

    def to_string(self):
        str = ""
        for r in self.grid:
            str += "".join(r)
        return str

    def part_two(self):
        cycle = 0
        history = [self.to_string()]
        while True:
            self.tip_cycle()
            history.append(self.to_string())
            cycle += 1
            # print(f'after {cycle} cycles')
            # for row in range(len(self.grid)):
            #     for col in range(len(self.grid[0])):
            #         print(f"{self.grid[row][col]} ", end='')
            #     print()
            if cycle == 1000000000:
                break
            if history.count(self.to_string()) == 2:
                goal = self.to_string()
                [first, last] = [i for i,x in enumerate(history) if x == goal]
                length = last - first
                todo = (1000000000 - cycle) % length
                for i in range(todo):
                    self.tip_cycle()
                break
        load = self.calculate_load_north()
        print(f"Total north load = {load}")
        return load


def main():
    """ stub for main() """
    aoc1 = Day14(file_to_string("data\\day14.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()

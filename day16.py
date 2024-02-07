""" Day 16 setup """

from advent import Advent, Runner, file_to_string
from queue import SimpleQueue

NORTH = 1
SOUTH = 2
EAST = 4
WEST = 8
deltas = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    EAST: (0, 1),
    WEST: (0, -1)
}

def get_dir( old_dir, ch ):
    if ch == '/':
        if old_dir == NORTH:
            return [EAST]
        elif old_dir == SOUTH:
            return [WEST]
        elif old_dir == EAST:
            return [NORTH]
        elif old_dir == WEST:
            return [SOUTH]
        else:
            raise Exception(f"bad direction {old_dir}")
    elif ch == '\\':
        if old_dir == NORTH:
            return [WEST]
        elif old_dir == SOUTH:
            return [EAST]
        elif old_dir == EAST:
            return [SOUTH]
        elif old_dir == WEST:
            return [NORTH]
        else:
            raise Exception(f"bad direction {old_dir}")
    elif ch == '|':
        if old_dir == NORTH or old_dir == SOUTH:
            return [old_dir]
        elif old_dir == EAST or old_dir == WEST:
            return [NORTH, SOUTH]
        else:
            raise Exception(f"bad direction {old_dir}")
    elif ch == '-':
        if old_dir == NORTH or old_dir == SOUTH:
            return [WEST, EAST]
        elif old_dir == EAST or old_dir == WEST:
            return [old_dir]
        else:
            raise Exception(f"bad direction {old_dir}")
    else:
        raise Exception(f"Bad character {ch}")

class Day16(Advent):
    """ Day 16 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "16"
        self.grid = []
        self.rows = None
        self.cols = None
        self.history = []

    def parse(self):
        for line in self.input_lines:
            self.grid.append(line)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        # for r in range(self.rows):
        #     for c in range(self.cols):
        #         print(self.grid[r][c], end='')
        #     print()

    def part_one(self):
        self.clear_history()
        self.inject_ray(0, 0, EAST)
        count = self.count_history()

        print(f"rays energized {count} locations")
        return count

    def inject_ray(self, start_r, start_c, start_dir):
        q = SimpleQueue()
        q.put((start_r, start_c, start_dir))
        while not q.empty():
            (r, c, old_dir) = q.get()

            if not (0 <= r < self.rows) or not (0 <= c < self.cols):
                continue
            if self.history[r][c] & old_dir > 0:
                continue

            self.history[r][c] |= old_dir
            while 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == '.':
                dr, dc = deltas[old_dir]
                r, c = r + dr, c + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    self.history[r][c] |= old_dir
            if 0 <= r < self.rows and 0 <= c < self.cols:
                for new_dir in get_dir(old_dir, self.grid[r][c]):
                    dr, dc = deltas[new_dir]
                    q.put((r + dr, c + dc, new_dir))

    def count_history(self):
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.history[r][c] > 0:
                    count += 1
        return count

    def clear_history(self):
        self.history = []
        for r in range(self.rows):
            history_row = []
            for c in range(self.cols):
                history_row.append(0)
            self.history.append(history_row)

    def part_two(self):
        counts = []
        for c in range(self.cols):
            self.clear_history()
            self.inject_ray(0, c, SOUTH)
            counts.append(self.count_history())

            self.clear_history()
            self.inject_ray(self.rows - 1, c, NORTH)
            counts.append(self.count_history())

        for r in range(self.rows):
            self.clear_history()
            self.inject_ray(r, 0, EAST)
            counts.append(self.count_history())

            self.clear_history()
            self.inject_ray(r, self.cols - 1, WEST)
            counts.append(self.count_history())

        max_count = max(counts)
        print(f"best ray energized {max_count} locations")
        return max_count


def main():
    """ stub for main() """
    aoc16 = Day16(file_to_string("data\\day16.txt"))
    runner = Runner(aoc16)
    runner.run()


if __name__ == '__main__':
    main()

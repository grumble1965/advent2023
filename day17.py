""" Day 17 setup """

from advent import Advent, Runner, file_to_string

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

PrintDirection = {
    NORTH: '^',
    EAST: '>',
    SOUTH: 'V',
    WEST: '<'
}

TurnLeft = {
    NORTH: WEST,
    EAST: NORTH,
    SOUTH: EAST,
    WEST: SOUTH
}

TurnRight = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

Deltas = {
    NORTH: (-1, 0),
    EAST: (0, 1),
    SOUTH: (1, 0),
    WEST: (0, -1)
}

ReverseDeltas = {
    (-1, 0): NORTH,
    (0, 1): EAST,
    (1, 0): SOUTH,
    (0, -1): WEST
}


class Cell:
    def __init__(self, r, c, value):
        self.r = r
        self.c = c
        self.value = value
        self.gScore = 1e9
        self.fScore = 1e9


class Day17(Advent):
    """ Day 17 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "17"
        self.grid = dict()
        self.rows = None
        self.cols = None

    def parse(self):
        self.rows = len(self.input_lines)
        self.cols = len(self.input_lines[0])
        for row in range(self.rows):
            line_array = self.input_lines[row]
            for col in range(self.cols):
                ch = line_array[col]
                cell = Cell(row, col, int(ch))
                self.grid[(row,col)] = cell

    def build_path(self, cameFrom, current):
        total_path = [current]
        while (current.r, current.c) in cameFrom.keys():
            current = self.grid[cameFrom[(current.r, current.c)]]
            total_path.insert(0, current)
        return total_path

    def get_neighbors(self, current, cameFrom):
        r, c = current.r, current.c
        neighbors = []

        if not (r,c) in cameFrom:
            # starting location only can move any direction but only east and south are valid
            for dir in [NORTH, SOUTH, EAST, WEST]:
                dr, dc = Deltas[dir]
                neighbors.append( (r + dr, c + dc) )
        else:
            # calculate the current direction of travel so we can find left and right turns
            p1 = cameFrom[(r,c)]
            d1 = (r - p1[0], c - p1[1])
            last_step = ReverseDeltas[d1]

            # add left and right turn steps
            for new_dir in [TurnLeft[last_step], TurnRight[last_step]]:
                dr, dc = Deltas[new_dir]
                neighbors.append((r + dr, c + dc))

            # get the last three steps (we know one)
            steps = [last_step]
            now = p1
            for i in range(2):
                if now in cameFrom:
                    prev = cameFrom[now]
                    d = (now[0] - prev[0], now[1] - prev[1])
                    steps.append(ReverseDeltas[d])
                    now = prev
                else:
                    steps.append(None)

            # if one of the last three steps was None, or we've turned
            # then straight ahead is a potential neighbor
            dr, dc = Deltas[last_step]
            straight = (r + dr, c + dc)
            if None in steps or steps.count(steps[0]) != len(steps):
                neighbors.append(straight)

        # now validate possible neighbors
        return [k for k in neighbors if (0 <= k[0] < self.rows) and (0 <= k[1] < self.cols)]

    def a_star(self, start, goal, heuristic):
        startCell = self.grid[start]
        goalCell = self.grid[goal]
        openSet = [startCell]
        cameFrom = dict()

        startCell.gScore = 0
        startCell.fScore = startCell.gScore + heuristic((startCell.r, startCell.c))

        while len(openSet) > 0:
            # current = (r,c) where fScore[(r,c)] is minimum
            best_fScore = 1e9
            current = None
            for kCell in openSet:
                if kCell.fScore < best_fScore:
                    best_fScore = kCell.fScore
                    current = kCell
            if current == goalCell:
                return self.build_path(cameFrom, current)

            openSet.remove(current)
            for neighbor in self.get_neighbors(current, cameFrom):
                nCell = self.grid[neighbor]
                tentative_gScore = current.gScore + nCell.value
                if tentative_gScore < nCell.gScore:
                    cameFrom[neighbor] = (current.r, current.c)
                    nCell.gScore = tentative_gScore
                    nCell.fScore = tentative_gScore + heuristic(neighbor)
                    if not nCell in openSet:
                        openSet.append(nCell)
        return None

    def part_one(self):
        h = lambda t : (self.rows - t[0] - 1) + (self.cols - t[1] - 1)
        p = self.a_star((0,0), (self.rows-1, self.cols-1), h)
        if p is None:
            print("No result")
            return None
        else:
            self.print_path(p)

            total = 0
            for k in p:
                if (k.r, k.c) != (0,0):
                    total += k.value
            print(f"Minimal heat loss is {total}")
            return total

    def print_path(self, p):
        # print([(cell.r,cell.c) for cell in p])
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[(r, c)]
                if cell in p:
                    idx = p.index(cell)
                    if idx > 0:  # no direction for first step
                        prevCell = p[idx - 1]
                        dr, dc = r - prevCell.r, c - prevCell.c
                        direct = ReverseDeltas[(dr, dc)]
                        print(PrintDirection[direct], end='')
                    else:
                        print(cell.value, end='')
                else:
                    print(cell.value, end='')
            print()

    def part_two(self):
        print(f"unsolved")
        return None


def main():
    """ stub for main() """
    aoc17 = Day17(file_to_string("data\\day17.txt"))
    runner = Runner(aoc17)
    runner.run()


if __name__ == '__main__':
    main()

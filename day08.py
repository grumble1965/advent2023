""" Day 08 setup """
import math

from advent import Advent, Runner, file_to_string

class Day08(Advent):
    """ Day 08 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "08"
        self.route = ""
        self.nodes = {}
        self.nodes_left = {}
        self.nodes_right = {}

    def parse(self):
        for line in self.input_lines:
            if len(line) > 0 and line.count(" ") == 0:
                self.route = line.strip()
                self.route_length = len(self.route)
            elif len(line) > 0:
                lhs, rhs = line.strip().split(' = ')
                rhs = rhs.replace('(', '')
                rhs = rhs.replace(')', '')
                left_node, right_node = rhs.split(', ')
                self.nodes[lhs] = (left_node, right_node)
                self.nodes_left[lhs] = left_node
                self.nodes_right[lhs] = right_node

    def infinite_directions(self, recipe):
        idx = 0
        while True:
            yield recipe[idx]
            idx += 1
            if idx >= len(recipe):
                idx = 0


    def part_one(self):
        # print(f"route: {self.route}")
        # for k,v in self.nodes.items():
        #     print(f"{k} -> {v}")

        location = 'AAA'
        num_steps = 0
        direction_generator = self.infinite_directions(self.route)
        while location != 'ZZZ':
            direction = next(direction_generator)
            num_steps += 1
            (left, right) = self.nodes[location]
            if direction == 'L':
                location = left
            elif direction == 'R':
                location = right
            else:
                raise Exception(f"Unknown direction {direction}")

        print(f"Reached ZZZ in {num_steps}")
        return num_steps

    def run_until_finish(self, start):
        trace = []
        direction_generator = self.infinite_directions(self.route)
        location = start
        while not location.endswith('Z'):
            trace.append(location)
            direction = next(direction_generator)
            (left, right) = self.nodes[location]
            if direction == 'L':
                location = left
            elif direction == 'R':
                location = right
        return trace

    def part_two(self):
        locations = list([x for x in self.nodes.keys() if x[-1] == 'A'])

        loops = {}
        for loc in locations:
            loops[loc] = self.run_until_finish(loc)

        lcm_input = []
        for k,v in loops.items():
            # print(f"{k} ends at {len(v)}")
            lcm_input.append(len(v))

        lcm = math.lcm(*lcm_input)
        print(f"Least common multiple is {lcm}")
        return lcm


def main():
    """ stub for main() """
    aoc08 = Day08(file_to_string("data\\day08.txt"))
    runner = Runner(aoc08)
    runner.run()

if __name__ == '__main__':
    main()

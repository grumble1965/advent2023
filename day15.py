""" Day 15 setup """

from advent import Advent, Runner, file_to_string


class Day15(Advent):
    """ Day 15 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text[0]
        self.name = "15"
        self.steps = []
        self.boxes = dict()
        for box_no in range(256):
            self.boxes[box_no] = []

    def parse(self):
        self.steps = self.input_lines.split(',')

    @staticmethod
    def hash_alg(str : str) -> int:
        current_value = 0
        for ch in str:
            current_value += ord(ch)
            current_value *= 17
            current_value %= 256
        return current_value

    def part_one(self):
        total = 0
        for st in self.steps:
            total += Day15.hash_alg(st)
        print(f"Sum of hash is {total}")
        return total

    def part_two(self):
        for st in self.steps:
            if '-' in st:
                end = st.find('-')
                box_name = st[:end]
                box_number = Day15.hash_alg(box_name)
                contents = self.boxes[box_number].copy()
                current = [i for i,x in enumerate(contents) if x[0] == box_name]
                if len(current) > 0:
                    # remove lens from contents
                    contents.pop(current[0])
                    self.boxes[box_number] = contents
            elif '=' in st:
                box_name, focal_str = st.split('=')
                box_number = Day15.hash_alg(box_name)
                contents = self.boxes[box_number].copy()
                current = [i for i,x in enumerate(contents) if x[0] == box_name]
                if len(current) > 0:
                    contents[current[0]] = (box_name, int(focal_str))
                else:
                    contents.append( (box_name, int(focal_str)) )
                self.boxes[box_number] = contents
            # print(f"after \"{st}\":")
            # for bn in range(256):
            #     if self.boxes[bn] != []:
            #         print(f"Box {bn}: {self.boxes[bn]}")
            # print()
        focus_power = 0
        for bn in range(256):
            contents = self.boxes[bn]
            if len(contents) > 0:
                for slot in range(len(contents)):
                    lens, focus = contents[slot]
                    focus_power += (bn + 1) * (slot + 1) * focus
        print(f"Total focus power = {focus_power}")
        return focus_power


def main():
    """ stub for main() """
    aoc15 = Day15(file_to_string("data\\day15.txt"))
    runner = Runner(aoc15)
    runner.run()


if __name__ == '__main__':
    main()

""" Day XX setup """

from advent import Advent, Runner, file_to_string


class DayXX(Advent):
    """ Day XX solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "XX"

    def parse(self):
        pass

    def part_one(self):
        print(f"unsolved")
        return None

    def part_two(self):
        print(f"unsolved")
        return None


def main():
    """ stub for main() """
    aocXX = DayXX(file_to_string("data\\dayXX.txt"))
    runner = Runner(aocXX)
    runner.run()


if __name__ == '__main__':
    main()

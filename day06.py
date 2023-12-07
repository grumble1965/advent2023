""" Day 06 setup """

from advent import Advent, Runner, file_to_string


class Day06(Advent):
    """ Day 06 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "06"
        self.races = []

    def parse(self):
        times = []
        records = []
        for line in self.input_lines:
            name, numbers = line.strip().split(": ")
            num_list = []
            for n in numbers.strip().split():
                num_list.append(int(n))
            if name == 'Time':
                times = num_list
            elif name == 'Distance':
                records = num_list
            else:
                raise Exception(f"Unknown name {name}")

        if len(times) == len(records):
            for i in range(len(times)):
                self.races.append( (times[i], records[i]) )
        else:
            raise Exception("mismatched input lists")


    def part_one(self):
        product = 1
        for t_max, d_min in self.races:
            wins = 0
            for button_time in range(t_max + 1):
                speed = button_time
                coast = t_max - button_time
                distance = coast * speed
                # print(f"Button down {button_time}:  Speed = {speed}  Distance = {distance}  Record = {d_min}")
                if distance > d_min:
                    # print("win!")
                    wins += 1
            # print(f"race {t_max}/{d_min}: wins = {wins}")
            product *= wins
        print(f"Product of total wins = {product}")
        return product

    def part_two(self):
        wins = 0
        time_str, dist_str = "", ""
        for t_max, d_min in self.races:
            time_str += f"{t_max}"
            dist_str += f"{d_min}"
        t_max, d_min = int(time_str), int(dist_str)
        for button_time in range(t_max + 1):
            speed = button_time
            coast = t_max - button_time
            distance = coast * speed
            # print(f"Button down {button_time}:  Speed = {speed}  Distance = {distance}  Record = {d_min}")
            if distance > d_min:
                # print("win!")
                wins += 1
        print(f"Total wins = {wins}")
        return wins


def main():
    """ stub for main() """
    aoc06 = Day06(file_to_string("data\\day06.txt"))
    runner = Runner(aoc06)
    runner.run()


if __name__ == '__main__':
    main()

""" Day 06 setup """
import math

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
                self.races.append((times[i], records[i]))
        else:
            raise Exception("mismatched input lists")

    def part_one(self):
        product = 1
        for t_max, d_min in self.races:
            wins = self.calculate_wins(d_min, t_max)
            product *= wins
        print(f"Product of total wins = {product}")
        return product

    def part_two(self):
        time_str, dist_str = "", ""
        for race_time, race_distance in self.races:
            time_str += f"{race_time}"
            dist_str += f"{race_distance}"
        race_time, race_distance = int(time_str), int(dist_str)

        wins = self.calculate_wins(race_distance, race_time)
        print(f"Total wins = {wins}")
        return wins

    def calculate_wins(self, race_distance, race_time):
        """ closed form determination of number of wins for a race """
        # distance = (race_time - button_time) * button_time
        # distance = -button^2 + race_time*button
        # distance - race_distance = -button^2 + race_time*button - race_distance
        # y = distance - race_distance
        # x = button
        # y = -x^2 + race_time*x -race_distance
        # y = ax^2 + bx + c
        # y = ( -race_time +/- sqrt(race_time^2 - 4 * (-1) * (-race_distance) ) / (2 * -1)

        a = -1
        b = race_time
        c = -race_distance
        deter = math.sqrt(b * b - (4.0 * a * c))
        first = math.ceil((-b + deter) / (2 * a))
        second = math.floor((-b - deter) / (2 * a))
        if first * (b - first) == race_distance:
            first += 1
        if second * (b - second) == race_distance:
            second -= 1
        return second - first + 1


def main():
    """ stub for main() """
    aoc06 = Day06(file_to_string("data\\day06.txt"))
    runner = Runner(aoc06)
    runner.run()


if __name__ == '__main__':
    main()

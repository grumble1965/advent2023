""" Day 2 setup """

from advent import Advent, Runner, file_to_string


class Day02(Advent):
    """ Day 2 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.games = []
        self.name = "2"

    def parse(self):
        for line in self.input_lines:
            this_game = []
            game, data = line.split(":")
            _, game_number = game.split()
            this_game.append(int(game_number))

            rounds = data.strip().split("; ")
            for this_round in rounds:
                r, g, b = 0, 0, 0
                for pair in this_round.strip().split(", "):
                    num, color = pair.strip().split(" ")
                    if color == 'red':
                        r = int(num)
                    elif color == 'green':
                        g = int(num)
                    elif color == 'blue':
                        b = int(num)
                    else:
                        pass
                this_game.append((r, g, b))
            self.games.append(this_game)

    def part_one(self):
        max_red, max_green, max_blue = 12, 13, 14
        possibles = 0
        for g in self.games:
            num = g[0]
            possible = True
            for r, g, b in g[1:]:
                if r > max_red or g > max_green or b > max_blue:
                    possible = False
                    break
            if possible:
                possibles += num
        print(f"Sum of possible games = {possibles}")
        return possibles

    def part_two(self):
        sum_power = 0
        for g in self.games:
            min_red, min_green, min_blue = 0, 0, 0
            num = g[0]
            for r, g, b in g[1:]:
                min_red = max(min_red, r)
                min_green = max(min_green, g)
                min_blue = max(min_blue, b)
            power = min_red * min_green * min_blue
            sum_power += power
            # print(f"game {num}: {min_red}, {min_green}, {min_blue} => {power}")
        print(f"Sum of powerset of all games = {sum_power}")
        return sum_power


def main():
    """ stub for main() """
    aoc2 = Day02(file_to_string("data\\day02.txt"))
    runner = Runner(aoc2)
    runner.run()


if __name__ == '__main__':
    main()

""" Day 4 setup """

from advent import Advent, Runner, file_to_string


class Day04(Advent):
    """ Day 4 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.winners = {}
        self.numbers = {}
        self.name = "4"

    def parse(self):
        for line in self.input_lines:
            front, rear = line.split(": ")
            _, card_str = front.split()
            card = int(card_str)
            winners, numbers = rear.split("| ")
            self.winners[card] = set(winners.strip().split())
            self.numbers[card] = set(numbers.strip().split())

    def part_one(self):
        total_points = 0
        for card in self.winners.keys():
            matches = len(self.winners[card].intersection(self.numbers[card]))
            if matches > 0:
                total_points += (2 ** (matches - 1))
        print(f"Total points = {total_points}")
        return total_points

    def part_two(self):
        deck = {}
        number_list = []
        for k in self.winners.keys():
            deck[k] = 1
            number_list.append(k)

        number_list.sort()
        for card in number_list:
            matches = len(self.winners[card].intersection(self.numbers[card]))
            if matches > 0:
                how_many = deck[card]
                for i in range(card + 1, card + matches + 1):
                    deck[i] += how_many

        total_cards = sum(deck.values())

        print(f"Total scratchcards = {total_cards}")
        return total_cards


def main():
    """ stub for main() """
    aoc4 = Day04(file_to_string("data\\day04.txt"))
    runner = Runner(aoc4)
    runner.run()


if __name__ == '__main__':
    main()

""" Day 09 setup """

from advent import Advent, Runner, file_to_string


class Day09(Advent):
    """ Day 09 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "09"
        self.sequences = []

    def parse(self):
        for line in self.input_lines:
            strs = line.strip().split()
            ints = list(map(lambda x: int(x), strs))
            self.sequences.append(ints)


    def solve_forward_sequence(self, seq):
        derived_sequences = [seq]
        this_seq = seq
        while True:
            new_seq = []
            for i in range(1, len(this_seq)):
                new_seq.append(this_seq[i] - this_seq[i - 1])
            derived_sequences.append(new_seq)
            if all(x == 0 for x in new_seq):
                break
            this_seq = new_seq
        # print("was")
        # for s in derived_sequences:
        #     print(f"{s}")
        # print()
        for idx in range(len(derived_sequences)-1, -1, -1):
            if idx == len(derived_sequences) - 1:
                new_value = 0
            else:
                new_value = derived_sequences[idx][-1] + derived_sequences[idx+1][-1]
            derived_sequences[idx].append(new_value)
        # print("becomes")
        # for s in derived_sequences:
        #     print(f"{s}")
        # print()
        return derived_sequences[0][-1]

    def solve_backward_sequence(self, seq):
        derived_sequences = [seq]
        this_seq = seq
        while True:
            new_seq = []
            for i in range(1, len(this_seq)):
                new_seq.append(this_seq[i] - this_seq[i - 1])
            derived_sequences.append(new_seq)
            if all(x == 0 for x in new_seq):
                break
            this_seq = new_seq
        # print("was")
        # for s in derived_sequences:
        #     print(f"{s}")
        # print()
        for idx in range(len(derived_sequences)-1, -1, -1):
            if idx == len(derived_sequences) - 1:
                new_value = 0
            else:
                new_value = derived_sequences[idx][0] - derived_sequences[idx+1][0]
            derived_sequences[idx].insert(0, new_value)
        # print("becomes")
        # for s in derived_sequences:
        #     print(f"{s}")
        # print()
        return derived_sequences[0][0]


    def part_one(self):
        total = 0
        for seq in self.sequences:
            next_value = self.solve_forward_sequence(seq)
            total += next_value
        print(f"Sum of extrapolated values = {total}")
        return total

    def part_two(self):
        total = 0
        for seq in self.sequences:
            next_value = self.solve_backward_sequence(seq)
            total += next_value
        print(f"Sum of extrapolated values = {total}")
        return total


def main():
    """ stub for main() """
    aoc09 = Day09(file_to_string("data\\day09.txt"))
    runner = Runner(aoc09)
    runner.run()


if __name__ == '__main__':
    main()

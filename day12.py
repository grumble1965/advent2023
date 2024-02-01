""" Day 12 setup """

from advent import Advent, Runner, file_to_string


class Day12(Advent):
    """ Day 12 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "12"
        self.lines = []
        self.expanded_lines = []

    def parse(self):
        for line in self.input_lines:
            pattern, spring_str = line.split()
            spring_list = self.string_int_list_to_int_list(spring_str)
            self.lines.append((pattern, spring_list))

            long_pattern = f"{pattern}?{pattern}?{pattern}?{pattern}?{pattern}"
            long_spring_str = f"{spring_str},{spring_str},{spring_str},{spring_str},{spring_str}"
            long_spring_list = self.string_int_list_to_int_list(long_spring_str)
            self.expanded_lines.append((long_pattern, long_spring_list))

    def string_int_list_to_int_list(self, spring_str):
        spring_str.lstrip('[')
        spring_str.rstrip(']')
        temp_list = spring_str.split(',')
        spring_list = [int(x) for x in temp_list]
        return spring_list

    def expand_pattern(self, pattern):
        pattern_queue = [pattern]
        while len(pattern_queue) > 0:
            p = pattern_queue.pop(0)
            if '?' not in p:
                yield p
            else:
                p1 = p.replace('?', '#', 1)
                p2 = p.replace('?', '.', 1)
                pattern_queue.insert(0, p1)
                pattern_queue.insert(0, p2)

    def unify(self, pattern, spring_list):
        pattern.strip('.')
        tmp_list = pattern.split('.')
        pattern_list = [len(x) for x in tmp_list if len(x) > 0]
        return len(pattern_list) == len(spring_list) and all([pattern_list[i] == spring_list[i] for i in range(len(pattern_list))])

    def part_one(self):
        total_arrangements = 0
        for pattern,springs in self.lines:
            line_arrangements = 0
            for pp in self.expand_pattern(pattern):
                if self.unify(pp, springs):
                    line_arrangements += 1
            total_arrangements += line_arrangements

        print(f"Total arrangements = {total_arrangements}")
        return total_arrangements

    def better_unify(self, pattern, digits):
        pattern.lstrip('.')
        while pattern and digits:
            n = digits[0]
            if all(ch in ['#','?'] for ch in pattern[:n]) and (n == len(pattern) or pattern[n] in ['.', '?']):
                # spring fits
                if len(pattern) > n:
                    # recurse
                    rest_total = self.better_unify(pattern[n:], digits[1:])
                    if rest_total >= 0:
                        return 1 + rest_total
                    else:
                        return -1

    def part_two(self):
        total_arrangements = 0
        # for pattern,springs in self.expanded_lines:
        #     total_arrangements += self.better_unify(pattern, springs)

        print(f"Total arrangements = {total_arrangements}")
        return total_arrangements


def main():
    """ stub for main() """
    aoc12 = Day12(file_to_string("data\\day12.txt"))
    runner = Runner(aoc12)
    runner.run()


if __name__ == '__main__':
    main()

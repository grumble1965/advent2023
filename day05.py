""" Day 5 setup """

from advent import Advent, Runner, file_to_string


class Day05(Advent):
    """ Day 5 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "5"
        self.seeds = []
        self.maps = {}

    def parse(self):
        map_name = None
        tmp_map = []
        for line in self.input_lines:
            if line.startswith("seeds:"):
                _, seeds = line.split(": ")
                seed_list = seeds.strip().split()
                for s in seed_list:
                    self.seeds.append(int(s))
            elif line.endswith(" map:"):
                map_name, _ = line.strip().split()
            elif len(line.strip().split()) == 3:
                nums = line.strip().split()
                tmp_map.append((int(nums[0]), int(nums[1]), int(nums[2])))
            elif line == "" and map_name is not None:
                self.maps[map_name] = tmp_map
                map_name, tmp_map = None, []
            else:
                pass
        if map_name is not None:
            self.maps[map_name] = tmp_map

    def mapper(self, table, input_value):
        output_value = None
        for dest_start, source_start, length in table:
            if source_start <= input_value <= source_start + length:
                offset = input_value - source_start
                output_value = dest_start + offset
                break
        if output_value is not None:
            return output_value
        else:
            return input_value

    def map_range(self, table, input_start, input_length):
        """
        given an input range (start and length), using the supplied table
        map that into one or more output ranges (start and length)
        """
        results = []
        while input_length > 0:
            row = None
            for i in range(len(table)):
                _,s,l = table[i]
                if l == float('inf') or s <= input_start < s + l:
                    row = table[i]
                    break
            if row is None:
                raise Exception(f"value {input_start} not found in table {table}")

            dest, source, length = row
            offset = input_start - source
            output_start = dest + offset
            if length == float('inf') or input_start + input_length < source + length:
                # fits in one range
                output_length = input_length
            else:
                # need multiple ranges
                output_length = length - offset
            results.append((output_start, output_length))
            input_start += output_length
            input_length -= output_length
        return results

    def fix_table(self, table):
        table.sort(key=lambda t: t[1])      # sort ascending by source_start

        # add ranges (if needed) between table_n and table_n+1
        to_add = []
        for i in range(len(table) - 1):
            last = table[i][1] + table[i][2]
            if last < table[i+1][1]:
                to_add.append( (last, last, table[i+1][1]-last) )
        for t in to_add:
            table.append(t)
        table.sort(key=lambda t: t[1])      # sort ascending by source_start

        # add zero .. first entry
        if table[0][1] > 0:
            table.insert(0, (0, 0, table[0][1]))

        # add last entry .. inf
        entry = table[-1]
        if entry[2] != float('inf'):
            tmp = entry[1] + entry[2]
            table.append( (tmp, tmp, float('inf')) )

        table.sort(key=lambda t: t[1])      # sort ascending by source_start
        return table

    def part_one(self):
        locations = []
        for seed in self.seeds:
            soil = self.mapper(self.maps['seed-to-soil'], seed)
            fertilizer = self.mapper(self.maps['soil-to-fertilizer'], soil)
            water = self.mapper(self.maps['fertilizer-to-water'], fertilizer)
            light = self.mapper(self.maps['water-to-light'], water)
            temperature = self.mapper(self.maps['light-to-temperature'], light)
            humidity = self.mapper(self.maps['temperature-to-humidity'], temperature)
            location = self.mapper(self.maps['humidity-to-location'], humidity)
            locations.append(location)
        lowest = min(locations)
        print(f"Lowest location: {lowest}")
        return lowest

    def apply_map_to_range(self, table, ranges):
        results = []
        for start, length in ranges:
            output_ranges = self.map_range(table, start, length)
            results.extend(output_ranges)
        return results

    def part_two(self):
        new_map = {}
        for k,v in self.maps.items():
            new_map[k] = self.fix_table(v)
        self.maps = new_map

        seed_ranges = []
        i = 0
        while i < len(self.seeds):
            start, length = self.seeds[i], self.seeds[i + 1]
            seed_ranges.append((start, length))
            i += 2

        soil_ranges = self.apply_map_to_range(self.maps['seed-to-soil'], seed_ranges)
        fertilizer_ranges = self.apply_map_to_range(self.maps['soil-to-fertilizer'], soil_ranges)
        water_ranges = self.apply_map_to_range(self.maps['fertilizer-to-water'], fertilizer_ranges)
        light_ranges = self.apply_map_to_range(self.maps['water-to-light'], water_ranges)
        temperature_ranges = self.apply_map_to_range(self.maps['light-to-temperature'], light_ranges)
        humidity_ranges = self.apply_map_to_range(self.maps['temperature-to-humidity'], temperature_ranges)
        location_ranges = self.apply_map_to_range(self.maps['humidity-to-location'], humidity_ranges)

        locations = []
        for start, _ in location_ranges:
            locations.append(start)

        lowest = min(locations)
        print(f"Lowest location: {lowest}")
        return lowest


def main():
    """ stub for main() """
    aoc5 = Day05(file_to_string("data\\day05.txt"))
    runner = Runner(aoc5)
    runner.run()


if __name__ == '__main__':
    main()

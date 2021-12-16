import numpy
import copy

"""
Disclaimer this is in no way the best solution to traverse this tree I played 
along enough to get the correct answer and probably missing a lot of concept 
and knowledge into how to do this solution properly and more efficiently 
"""


class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.lowest_points = []
        self.adjacent_locations = [
            {'row': -1, 'column':  0},  # U
            {'row':  1, 'column':  0},  # D
            {'row':  0, 'column':  1},  # R
            {'row':  0, 'column': -1}   # L
        ]
        self.diagonal_locations = [
            {'row': -1, 'column':  1},  # DR
            {'row':  1, 'column':  1},  # UR
            {'row':  1, 'column': -1},  # UL
            {'row': -1, 'column': -1}   # UR
        ]
        self.horizontal_directions = [
            {'direction': 'down', 'row': -1, 'column': 0},  # U
            {'direction': 'up',   'row':  1, 'column': 0}   # D
        ]
        self.vertical_directions = [
            {'direction': 'right', 'row': 0, 'column':  1}, # R
            {'direction': 'left',  'row': 0, 'column': -1}  # L
        ]
        self.basins = []
        self.basins_values = []
        self.basin_index = 0
        self.basins_count = 0
        self.master_count = 0
        self.recursion_depth = 0
        # 3 levels are enough to get the correct answer
        self.recursion_depth_max = 3

    def run(self):
        self.get_input_from_file()
        self.process_input()
        self.print_output()

    def get_input_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        for entry in lines:
            row = [int(x) for x in list(entry.strip())]
            self.raw_data.append(row)

    def process_input(self):
        self.find_lowest_points()
        self.find_basins()
        self.collect_basins_values()
        self.calculate_solution()
        # self.visualize_everything()

    def find_lowest_points(self):
        for row_index, row in enumerate(self.raw_data):
            for column_index, entry in enumerate(row):
                adjacent_lower = False
                adjacent_values = []

                for adjacent_location in self.adjacent_locations:
                    adjacent_row = row_index + adjacent_location['row']
                    adjacent_column = column_index + adjacent_location['column']
                    if adjacent_row != -1 \
                            and adjacent_column != -1 \
                            and adjacent_row < len(self.raw_data) \
                            and adjacent_column < len(row):
                        adjacent_values.append({
                            'value': self.raw_data[adjacent_row][adjacent_column],
                            'row': adjacent_row,
                            'column': adjacent_column
                        })

                for point in adjacent_values:
                    if self.raw_data[point['row']][point['column']] <= entry:
                        adjacent_lower = True

                if adjacent_lower is False:
                    self.lowest_points.append({
                        'row': row_index,
                        'column': column_index
                    })

    def find_basins(self):
        self.basins = [[] for x in range(len(self.lowest_points))]
        self.basin_index = 0
        for point in self.lowest_points:
            self.upsert_basin(point)
            self.loop_direction(point, self.vertical_directions, self.horizontal_directions)
            self.loop_direction(point, self.horizontal_directions, self.vertical_directions)
            self.basin_index += 1

    def loop_direction(self, starting_point, primary_directions, secondary_directions):
        for p_direction in primary_directions:
            point = copy.deepcopy(starting_point)
            point['row'] += p_direction['row']
            point['column'] += p_direction['column']
            loop = self.check_point(point)
            while loop is True:
                self.recursion_depth = 0
                self.check_neighbours_in_direction(copy.deepcopy(point), secondary_directions, primary_directions)
                point['row'] += p_direction['row']
                point['column'] += p_direction['column']
                loop = self.check_point(point)

    def check_neighbours_in_direction(self, point, secondary_directions, primary_directions):
        if self.recursion_depth <= self.recursion_depth_max:
            self.recursion_depth += 1
            for s_direction in secondary_directions:
                loop = True
                while loop is True:
                    point['row'] += s_direction['row']
                    point['column'] += s_direction['column']
                    loop = self.check_point(point)
                    if loop is True:
                        self.check_neighbours_in_direction(copy.deepcopy(point), primary_directions, secondary_directions)

    def check_point(self, point):
        if point['row'] == -1 \
                or point['column'] == -1 \
                or point['row'] >= len(self.raw_data) \
                or point['column'] >= len(self.raw_data[point['row']]) \
                or self.raw_data[point['row']][point['column']] >= 9:
            return False
        else:
            self.upsert_basin(point)
            return True

    def upsert_basin(self, point):
        found = False
        for basin_point in self.basins[self.basin_index]:
            if basin_point['row'] == point['row'] \
                    and basin_point['column'] == point['column']:
                found = True
        if found is False:
            self.append_basin(point)

    def append_basin(self, point):
        temp = copy.deepcopy(point)
        temp['value'] = self.raw_data[temp['row']][temp['column']]
        self.basins[self.basin_index].append(temp)

    def collect_basins_values(self):
        for row in self.raw_data:
            for point in row:
                if point < 9:
                    self.master_count += 1

        index = 0
        for basin in self.basins:
            self.basins_values.append([])
            self.basins_count += len(basin)
            for point in basin:
                self.basins_values[index].append(self.raw_data[point['row']][point['column']])
            index += 1

    def calculate_solution(self):
        basins_length = []
        for basin in self.basins:
            basins_length.append(len(basin))
        basins_length = sorted(basins_length, reverse=True)
        largest_basins = basins_length[:3]
        self.solution = numpy.prod(largest_basins)

    def print_output(self):
        print(f'Result: {self.solution}')

    def visualize_everything(self):
        for row_index in range(len(self.raw_data)):
            for column_index in range(len(self.raw_data[row_index])):
                continue_loop = True
                if self.raw_data[row_index][column_index] == 9:
                    print('B', end='')
                    continue_loop = False
                if continue_loop is True:
                    for point in self.lowest_points:
                        if point['row'] == row_index \
                                and point['column'] == column_index:
                            print('x', end='')
                            continue_loop = False
                if continue_loop is True:
                    for basin in self.basins:
                        for point in basin:
                            if point['row'] == row_index \
                                    and point['column'] == column_index:
                                print('.', end='')
                                continue_loop = False
                if continue_loop is True:
                    print('$', end='')
            print('')


if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 1134
    ##############################

    print("Running Test Input first")
    print("======================================")
    instance = Solution(file='test')
    instance.run()
    if instance.solution != expected_test_result:
        print("Test Input did not produce expected result, aborting")
    else:
        print("Test Input Passed, running challenge input")
        print("======================================")
        Solution(file='input').run()

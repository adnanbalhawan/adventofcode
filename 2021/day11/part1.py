import copy


class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.steps = 100
        self.flashes = 0
        self.current_step_flashed_points = []
        self.adjacent_locations = [
            {'direction':  'U', 'row': -1, 'column':  0},  # U
            {'direction':  'D', 'row':  1, 'column':  0},  # D
            {'direction':  'R', 'row':  0, 'column':  1},  # R
            {'direction':  'L', 'row':  0, 'column': -1},  # L
            {'direction': 'UR', 'row': -1, 'column':  1},  # UR
            {'direction': 'DR', 'row':  1, 'column':  1},  # DR
            {'direction': 'DL', 'row':  1, 'column': -1},  # DL
            {'direction': 'UL', 'row': -1, 'column': -1}   # UL
        ]

    def run(self):
        # Custom Function
        self.get_input_from_file()
        self.parse_input()
        self.process_input()
        self.print_output()

    def get_input_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        for entry in lines:
            self.raw_data.append(list(map(int, entry.strip())))

    def parse_input(self):
        # parse input in intended logic
        pass

    def process_input(self):
        for step in range(self.steps):
            self.current_step_flashed_points = []
            for row_index, row in enumerate(self.raw_data):
                for column_index, entry in enumerate(row):
                    self.energize_point(row_index, column_index)
        self.solution = self.flashes

    # custom functions go here
    def energize_point(self, row, column):
        if self.raw_data[row][column] < 9 and self.check_if_entry_in_flashed(row, column) is False:
            self.raw_data[row][column] += 1
        elif self.raw_data[row][column] >= 9:
            self.flash_entry(row, column)

    def flash_entry(self, row, column):
        self.current_step_flashed_points.append({
            'row': row,
            'column': column
        })
        self.flashes += 1
        self.raw_data[row][column] = 0
        self.energize_adjacent_locations({
            'row': row,
            'column': column
        })

    def energize_adjacent_locations(self, point):
        for direction in self.adjacent_locations:
            direction_row = point['row'] + direction['row']
            direction_column = point['column'] + direction['column']
            self.check_point(
                direction_row,
                direction_column
            )

    def check_point(self, row, column):
        if row == -1 \
                or column == -1 \
                or row >= len(self.raw_data) \
                or column >= len(self.raw_data[row]):
            return
        self.energize_point(row, column)

    def check_if_entry_in_flashed(self, row, column):
        for entry in self.current_step_flashed_points:
            if entry['row'] == row and entry['column'] == column:
                return True
        return False

    def print_output(self):
        print(f'Result: {self.solution}')


if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 1656
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
        instance = Solution(file='input').run()
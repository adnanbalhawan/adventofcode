class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.lowest_points = []
        self.adjacent_locations = [
            {'row': -1, 'column':  0}, # U
            {'row':  1, 'column':  0}, # D
            {'row':  0, 'column':  1}, # R
            {'row':  0, 'column': -1}  # L
        ]

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
        for entry in self.lowest_points:
            self.solution += entry['value'] + 1

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
                        'value': self.raw_data[row_index][column_index],
                        'row': row_index,
                        'column': column_index
                    })

    def print_output(self):
        print(f'Result: {self.solution}')


if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 15
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

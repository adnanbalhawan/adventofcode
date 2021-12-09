class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.lines_coordinates = []
        self.furthest_coordinates = [0, 0]
        self.plot_area = []

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
            self.raw_data.append(entry.strip())

    def parse_input(self):
        # parse input in intended logic
        for line in self.raw_data:
            line_coordinates = []
            parsed_line = line.split(' -> ')
            for point in parsed_line:
                point_coordinates = point.split(',')
                for index in range(len(point_coordinates)):
                    point_coordinates[index] = int(point_coordinates[index])
                line_coordinates.append(point_coordinates)
            self.lines_coordinates.append(line_coordinates)
    
    def process_input(self):
        self.get_furthest_points()
        self.generate_plot_area()
        self.draw_lines()
        self.count_dangerous_overlaps()
    
    #custom functions go here
    def get_furthest_points(self):
        for line in self.lines_coordinates:
            for point in line:
                for index in range(2):
                    self.furthest_coordinates[index] = point[index] + 1 if point[index] + 1 > self.furthest_coordinates[0] else self.furthest_coordinates[index]

    def generate_plot_area(self):
        self.plot_area = [[0] * self.furthest_coordinates[0] for i in range(self.furthest_coordinates[0])]

    def draw_lines(self):
        for line in self.lines_coordinates:
            start = line[0]
            end  = line[1]
            if start[0] == end[0]:
                if start[1] > end[1]:
                    loop_range = range(end[1], start[1] + 1)
                else:
                    loop_range = range(start[1], end[1] + 1)
                for colum_step in loop_range:
                    self.plot_area[start[0]][colum_step] += 1

            elif start[1] == end[1]:
                if start[0] > end[0]:
                    loop_range = range(end[0], start[0] + 1)
                else:
                    loop_range = range(start[0], end[0] + 1)
                for row_step in loop_range:
                    self.plot_area[row_step][start[1]] += 1                    

            
    def count_dangerous_overlaps(self):
        for row in self.plot_area:
            for point in row:
                if point >= 2:
                    self.solution += 1

    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 5
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

class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.point_scale = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        self.open_chars     = ['(', '[', '{', '<']
        self.closing_chars  = [')', ']', '}', '>']
        self.chars_stack = []
        self.corrupted_chars_count = {
            ')': 0,
            ']': 0,
            '}': 0,
            '>': 0
        }

    def run(self):
        # Custom Function
        self.get_input_from_file()
        self.parse_input()
        self.process_input()
        self.calculate_solution()
        self.print_output()

    def get_input_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        for entry in lines:
            self.raw_data.append(entry.strip())

    def parse_input(self):
        # parse input in intended logic
        pass

    def process_input(self):
        for line in self.raw_data:
            self.check_line(line)

    # custom functions go here
    def check_line(self, line):
        stack = []
        for char in line:
            if char in self.open_chars:
                stack.append(char)
            elif char in self.closing_chars:
                check_char = stack.pop()
                char_index = self.closing_chars.index(char)
                if check_char != self.open_chars[char_index]:
                    self.corrupted_chars_count[char] += 1

    def calculate_solution(self):
        for char in self.corrupted_chars_count:
            self.solution += self.point_scale[char] * self.corrupted_chars_count[char]

    def print_output(self):
        print(f'Result: {self.solution}')


if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 26397
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

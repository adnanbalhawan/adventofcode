class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.point_scale = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
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
        self.closing_char_sequences = []
        self.sequence_scores = []

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
        self.remove_corrupted_lines()
        for line in self.raw_data:
            unfinished_stack = self.collect_unfinished_sequences(line)
            self.generate_closing_sequence(unfinished_stack)

    # custom functions go here
    def remove_corrupted_lines(self):
        for line_index, line in enumerate(self.raw_data):
            stack = []
            for char in line:
                if char in self.open_chars:
                    stack.append(char)
                elif char in self.closing_chars:
                    char_index = self.closing_chars.index(char)
                    if len(stack) > 0 \
                            and stack[-1] == self.open_chars[char_index]:
                        stack.pop()
                    else:
                        self.raw_data.pop(line_index)
                        return self.remove_corrupted_lines()
        return

    def collect_unfinished_sequences(self, line):
        stack = []
        for char in line:
            if char in self.open_chars:
                stack.append(char)
            elif char in self.closing_chars:
                char_index = self.closing_chars.index(char)
                if stack[-1] == self.open_chars[char_index]:
                    stack.pop()
                else:
                    pass
        return stack

    def generate_closing_sequence(self, stack):
        sequence = []
        for char in stack:
            char_index = self.open_chars.index(char)
            sequence.append(self.closing_chars[char_index])
        sequence.reverse()
        self.closing_char_sequences.append(sequence)

    def calculate_solution(self):
        self.calculate_sequence_scores()
        self.solution = self.find_middle_score()

    def calculate_sequence_scores(self):
        for sequence in self.closing_char_sequences:
            score = 0
            for char in sequence:
                score *= 5
                score += self.point_scale[char]
            self.sequence_scores.append(score)
        self.sequence_scores = sorted(self.sequence_scores)

    def find_middle_score(self):
        middle_index = int(len(self.sequence_scores) / 2)
        return self.sequence_scores[middle_index]

    def print_output(self):
        print(f'Result: {self.solution}')


if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 288957
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

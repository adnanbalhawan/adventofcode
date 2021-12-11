class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.rule_set = [2, 3, 4, 7]

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
        for entry in self.raw_data:
            combination = entry.split(' | ')
            self.parsed_input.append({
                'signal_patterns': combination[0].split(' '),
                'output': combination[1].split(' ')
            })
        for row in self.parsed_input:
            print(row['signal_patterns'])
            print(row['output'])
            print('--------------------')
    
    def process_input(self):
        for screen in self.parsed_input:
            for output in screen['output']:
                if len(output) in self.rule_set:
                    self.solution += 1
    
    #custom functions go here
    
    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 26
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

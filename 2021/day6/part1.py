class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.simulation_days = 80
        self.new_lanternfish_timer = 8
        self.existing_lanternfish_timer = 6
        self.current_lanternfish = []
        
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
            for number in entry.split(','):
                self.current_lanternfish.append(int(number))                

    def parse_input(self):
        # parse input in intended logic
        pass
    
    def process_input(self):
        for day in range(self.simulation_days):
            self.check_lanterns_timers()
        self.solution = len(self.current_lanternfish)
   
    #custom functions go here
    def check_lanterns_timers(self):
        new_born_count = 0
        for index in range(len(self.current_lanternfish)):
            if self.current_lanternfish[index] == 0:
                new_born_count += 1
                self.current_lanternfish[index] = self.existing_lanternfish_timer
            elif self.current_lanternfish[index] > 0:
                self.current_lanternfish[index] -= 1
        for new_born in range(new_born_count):
            self.current_lanternfish.append(self.new_lanternfish_timer)
    
    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 5934
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

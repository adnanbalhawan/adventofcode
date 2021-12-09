class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.simulation_days = 256
        self.new_lanternfish_timer = 8
        self.existing_lanternfish_timer = 6
        self.current_lanternfish = []
        self.lantern_stats = []
        
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
        self.categorize_lanterns()
        for day in range(self.simulation_days):
            self.check_lanterns_timers()
        self.calculate_solution()
   
    #custom functions go here
    def categorize_lanterns(self):
        for timer in range(self.new_lanternfish_timer + 1):
            self.lantern_stats.append(0)
        for lantern in self.current_lanternfish:            
            self.lantern_stats[lantern] += 1
        print(self.lantern_stats)

    def check_lanterns_timers(self):
        new_born_count = self.lantern_stats[0]

        for timer in range(8):
            self.lantern_stats[timer] = self.lantern_stats[timer + 1]

        # new born lanterns and timer resets!!
        self.lantern_stats[8] = new_born_count
        self.lantern_stats[6] += new_born_count
        
    def calculate_solution(self):
        for lantern_timer in self.lantern_stats:
            self.solution += lantern_timer
    
    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 26984457539
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

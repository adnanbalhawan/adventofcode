class Solution():
    def __init__(self, file):
        self.file = file
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.max_position = 0
        self.horizontal_plane = []
        self.moving_costs = []

    def run(self):
        # Custom Function
        self.get_input_from_file()
        self.process_input()
        self.print_output()


    def get_input_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        for entry in lines[0].split(','):
            self.parsed_input.append(int(entry))
    
    def process_input(self):
        self.get_max_position()
        self.calculate_moving_fuel_cost()
        self.get_lowest_cost()
        
    #custom functions go here
    def get_max_position(self):
        for position in self.parsed_input:
            if position > self.max_position:
                self.max_position = position
    
    def calculate_moving_fuel_cost(self):
        for target_position_index in range(self.max_position):
            cost = 0
            for crab in self.parsed_input:
                cost += abs(crab - target_position_index)
            # print(f"cost at position {target_position_index} is {cost}")
            self.moving_costs.append({'pos': target_position_index, 'cost': cost})

    def get_lowest_cost(self):
        lowest = {'pos': None, 'cost': None}
        for cost in self.moving_costs:
            if lowest['cost'] is None or cost['cost'] < lowest['cost'] :
                lowest = cost
        self.solution = lowest['cost']

    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 37
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

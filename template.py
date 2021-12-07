class Solution():
    def __init__(self, file):
        self.file = file
        self.solution = 0
        self.get_data_from_file()
        # Custom Variables


    def run(self):
        # Custom Function

        self.print_output()
        
    def print_output(self):
        print(f'solution: {self.solution}')

    def get_data_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        self.data = []
        for entry in lines:
            self.data.append(entry.strip())



if __name__ == '__main__':
    file = 'test'
    expected_test_result = 0
    instance = Solution(file)
    instance.run()
    if instance.solution != expected_test_result:
        print("TEST Failed, aborting")
    else:
        file = 'input'
        instance = Solution(file).run()

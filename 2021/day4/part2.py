class Solution():
    def __init__(self, file):
        self.file = file
        self.solution = 0
        # Custom Variables
        self.bingo_input = []
        self.bingo_boards = []
        self.sum_of_unmarked = 0
        self.get_data_from_file()
        self.winning_boards = []

    def run(self):
        # Custom Function
        self.get_input()
        self.generate_bingo_boards_from_input()
        self.process_input()
        self.calculate_winning_board()
        self.print_output()
    
    def print_output(self):
        print(f'Sum of unmarked numbers: {self.sum_of_unmarked}, last called: {self.last_called_number}')
        self.solution = self.sum_of_unmarked * self.last_called_number
        print(f'Result: {self.solution}')

    def get_data_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        self.data = []
        for entry in lines:
            self.data.append(entry.strip())
        
    def get_input(self):
        # Get input and remove from Data
        input_data = self.data[0].split(',')
        self.data.remove(self.data[0])
        for entry in input_data:
            self.bingo_input.append(int(entry))
        # print(self.bingo_input)

    def get_board_structure(self):
        return [ [{'v': 0, 'm': False} for entry in range(5)] for row in range(5)]

    def generate_bingo_boards_from_input(self):
        board_index = -1
        board_row_index = 0
        board_row_number_index = 0
        for line in self.data:
            if line == '' or line == '\n':
                board_index += 1
                board_row_index = 0
                board_row_number_index = 0
                self.bingo_boards.insert(board_index, self.get_board_structure())
            else:
                line_data = line.split(' ')
                for number in line_data:
                    if number != '':
                        self.bingo_boards[board_index][board_row_index][board_row_number_index]['v'] = int(number)
                        board_row_number_index += 1
                board_row_number_index = 0
                board_row_index += 1
    
    def process_input(self):
        for called_number in self.bingo_input:
            # print(f'Calling: {called_number}')
            self.last_called_number = called_number
            self.flip_markers(called_number)
            self.check_winning_boards()
            if len(self.winning_boards) == len(self.bingo_boards):
                print("all boards won")
                return

    def flip_markers(self, called_number):        
        for board in self.bingo_boards:
            for row in board:
                for entry in row:
                    if entry['v'] == called_number:
                        entry['m'] = True
    
    def check_winning_boards(self):
        for board_index in range(len(self.bingo_boards)):

            for column_index in range(5):
                column_win_flag = True
                for row_index in range(5):
                    if self.bingo_boards[board_index][row_index][column_index]['m'] is False:
                        column_win_flag = False
                if column_win_flag is True:
                    self.add_to_winning_boards(board_index)

            for row in self.bingo_boards[board_index]:
                row_win_flag = True
                for entry in row:
                    if entry['m'] is False:
                        row_win_flag = False
                if row_win_flag is True:
                    self.add_to_winning_boards(board_index)             

    def add_to_winning_boards(self, winning_board):
        found = False
        for existing_winning_board in self.winning_boards:
            if existing_winning_board == winning_board:
                found = True
        if found is False:
            self.winning_boards.append(winning_board)

    def calculate_winning_board(self):
        for row in self.bingo_boards[self.winning_boards[-1]]:
            for entry in row:
                if entry['m'] is False:
                    self.sum_of_unmarked += entry['v']
        

if __name__ == '__main__':
    file = 'test'
    expected_test_result = 1924
    instance = Solution(file)
    instance.run()
    if instance.solution != expected_test_result:
        print("TEST Failed, aborting")
    else:
        file = 'input'
        instance = Solution(file).run()

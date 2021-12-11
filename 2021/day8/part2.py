import copy


class Solution():
    def __init__(self, file):
        self.file = file
        self.screen = {}
        self.screen_template = {
            'signal_patterns': [],
            'output': [],
            'mapping': { 'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''},
            'counts': { 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0},
            'mapped_output': [],
            'resolved_output': [],
            'resolved_output_number': []
        }
        self.raw_data = []
        self.parsed_input = []
        self.solution = 0
        # Custom Variables
        self.rule_set = [
            # {'number': 1, 'count': 2},
            # {'number': 7, 'count': 3},
            # {'number': 4, 'count': 4},
            {'number': 8, 'count': 7}
        ]
        self.number_segment_mapping = [
            ['a', 'b', 'c',      'e', 'f', 'g'], # 0
            [          'c',           'f'     ], # 1
            ['a',      'c', 'd', 'e',      'g'], # 2
            ['a',      'c', 'd',      'f', 'g'], # 3
            [     'b', 'c', 'd',      'f',    ], # 4
            ['a', 'b',      'd',      'f', 'g'], # 5
            ['a', 'b',      'd', 'e', 'f', 'g'], # 6
            ['a',      'c',           'f',    ], # 7
            ['a', 'b', 'c', 'd', 'e', 'f', 'g'], # 8
            ['a', 'b', 'c', 'd',      'f', 'g']  # 9
        ]
        self.number_segments = {}

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
        for index, number_segment in enumerate(self.number_segment_mapping):
            segment = ''.join(number_segment)
            self.number_segments[segment] = index

        for entry in self.raw_data:
            combination = entry.split(' | ')
            screen = copy.deepcopy(self.screen_template)
            screen['signal_patterns'] = combination[0].split(' ')
            screen['output'] = combination[1].split(' ')
            self.parsed_input.append(screen)
    
    def process_input(self):
        for screen in self.parsed_input:
            self.screen = screen
            self.count_digits()
            self.resolve_known_positions()
            self.resolve_positions()
            self.generate_pattern_output()
    
    def print_output(self):
        print('====================================')
        for row in self.parsed_input:
            print('--------------------')
            print(row['signal_patterns'])
            print(row['output'])
            for char, mapped in enumerate(row['mapping']):
                print(f"{mapped}: {row['mapping'][mapped]}")
        print('====================================')

    def count_digits(self):
        for word in self.screen['signal_patterns']:
            for char in word:
                self.screen['counts'][char] += 1
    
    def resolve_known_positions(self):
        for char in self.screen['counts']:
            if self.screen['counts'][char] == 6:
                self.screen['mapping']['b'] = char
            elif self.screen['counts'][char] == 4:
                self.screen['mapping']['e'] = char
            elif self.screen['counts'][char] == 9:
                self.screen['mapping']['f'] = char

    def resolve_positions(self):
        one = ''
        seven = ''
        four = ''
        eight = ''
        for word in self.screen['signal_patterns']:
            if len(word) == 2:
                one = word
            elif len(word) == 3:
                seven = word
            elif len(word) == 4:
                four = word
            elif len(word) == 7:
                eight = word
        
        # remove all one chars from 4 to solve 'd'
        # remove c and f, and known b
        for char in one:
            four = four.replace(char, '')
        four = four.replace(self.screen['mapping']['b'], '')
        self.screen['mapping']['d'] = four

        # solve f to find a and c from 7 & 1
        one = one.replace(self.screen['mapping']['f'], '')
        seven = seven.replace(self.screen['mapping']['f'], '')
        
        # solve c by matching remaining char in 1 and 7
        for one_char in one:
            for seven_char in seven:
                if one_char == seven_char:
                    self.screen['mapping']['c'] = one_char
        
        # solve a by removing remaining c in 7
        seven = seven.replace(self.screen['mapping']['c'], '')
        self.screen['mapping']['a'] = seven

        for char in eight:
            found = False
            for mapped_char in self.screen['mapping']:
                if self.screen['mapping'][mapped_char] == char:
                    found = True
            if found is False:
                self.screen['mapping']['g'] = char
    
    def generate_pattern_output(self):
        for output_word in self.screen['output']:
            mapped_word = []
            for output_word_char in output_word:
                for mapped_letter in self.screen['mapping']:
                    if output_word_char == self.screen['mapping'][mapped_letter]:
                        mapped_word.append(mapped_letter)
            self.screen['mapped_output'].append(sorted(mapped_word))
            for number, segment in enumerate(self.number_segments):
                if segment == ''.join(sorted(mapped_word)):
                    self.screen['resolved_output'].append(number)
        self.screen['resolved_output_number'] = ''.join(map(str, self.screen['resolved_output']))
        self.solution += int(self.screen['resolved_output_number'])
    
    def print_output(self):
        print(f'Result: {self.solution}')
        

if __name__ == '__main__':
    ##############################
    #### Expected Test Input Value
    expected_test_result = 5353
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

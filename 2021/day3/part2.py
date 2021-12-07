class Solution():
    def __init__(self, file):
        self.file = file
        self.solution = 0
        self.get_data_from_file()
        self.o2_generator_entries = self.data
        self.o2_generator_rating = 0
        self.o2_generator_rating_binary = 0
        self.co2_scrubber_entries = self.data
        self.co2_scrubber_rating = 0
        self.co2_scrubber_rating_binary = 0
        self.life_support_rating = 0

    def run(self):
        self.process_oxygen_generator_entries()
        self.process_co2_scrubber_entries()
        self.o2_generator_rating = int(self.o2_generator_rating_binary, 2)
        self.co2_scrubber_rating = int(self.co2_scrubber_rating_binary, 2)
        self.life_support_rating = self.o2_generator_rating * self.co2_scrubber_rating
        self.solution = self.life_support_rating
        self.print_output()
        
    def print_output(self):
        print(f'Oxygen Generator Rating, binary: {self.o2_generator_rating_binary}, int: {self.o2_generator_rating}')
        print(f'CO2 Scrubber Rating, binary: {self.co2_scrubber_rating_binary}, int: {self.co2_scrubber_rating}')
        print(f'life support rating: {self.life_support_rating}')

    def get_data_from_file(self):
        file = open(self.file, 'r')
        lines = file.readlines()
        self.data = []
        for entry in lines:
            self.data.append(entry.strip())

    def generate_positional_stats(self, data):
        positional_stats = []
        for entry in data:
            for char_index in range(len(entry)):
                if entry[char_index] != '\n':
                    try:
                        positional_stats[char_index][int(entry[char_index])] += 1
                    except IndexError as e:
                        positional_stats.append([0, 0])
                        positional_stats[char_index][int(entry[char_index])] += 1
                    # print(char_index, entry[char_index], positional_stats[char_index], positional_stats)
        return positional_stats
    
    def process_oxygen_generator_entries(self, current_index=0):
        # print('-------------------------------------------------------------------------------------')
        if len(self.o2_generator_entries) == 1:
            self.o2_generator_rating_binary = self.o2_generator_entries[0]
            return

        positional_stats = self.generate_positional_stats(self.o2_generator_entries)
        # print(f'position: {current_index}, stats: {positional_stats[current_index]}')
        if positional_stats[current_index][0] > positional_stats[current_index][1]:
            # print(f'dominant char is 0 so keep only the numbers with a 0 in the {current_index} position')
            self.o2_generator_entries = self.filter_array_entries(self.o2_generator_entries, current_index, '0')
        elif positional_stats[current_index][1] >= positional_stats[current_index][0]:
            # print(f'dominant char is 1 so keep only the numbers with a 0 in the {current_index} position')
            self.o2_generator_entries = self.filter_array_entries(self.o2_generator_entries, current_index, '1')
        
        # If we are at the last index, reset
        if current_index + 1 >= len(self.o2_generator_entries[0]):
            current_index = 0
        else: current_index += 1

        self.process_oxygen_generator_entries(current_index)
    
    def process_co2_scrubber_entries(self, current_index=0):
        # print('-------------------------------------------------------------------------------------')
        if len(self.co2_scrubber_entries) == 1:
            self.co2_scrubber_rating_binary = self.co2_scrubber_entries[0]
            return

        positional_stats = self.generate_positional_stats(self.co2_scrubber_entries)
        # print(f'position: {current_index}, stats: {positional_stats[current_index]}')
        if positional_stats[current_index][0] > positional_stats[current_index][1]:
            # print(f'dominant char is 0 so keep only the numbers with a 0 in the {current_index} position')
            self.co2_scrubber_entries = self.filter_array_entries(self.co2_scrubber_entries, current_index, '1')
        elif positional_stats[current_index][1] >= positional_stats[current_index][0]:
            # print(f'dominant char is 1 so keep only the numbers with a 0 in the {current_index} position')
            self.co2_scrubber_entries = self.filter_array_entries(self.co2_scrubber_entries, current_index, '0')
        
        # If we are at the last index, reset
        if current_index + 1 >= len(self.co2_scrubber_entries[0]):
            current_index = 0
        else: current_index += 1

        self.process_co2_scrubber_entries(current_index)

    def filter_array_entries(self, list, index, charToMatch):
        newList = []
        # print(f'filter list entries, {len(list)}')
        if len(list) == 1:
            return list[0]
        for entry in list:
            if entry[index] == charToMatch:
                # print(f'adding entry {entry}, entry_index: {entry[index]}, index_at: {index}, char to match: {charToMatch}')
                # print(f'og_list: {list}')
                newList.append(entry)
                # print(f'new List: {newList}')
        return newList


if __name__ == '__main__':
    file = 'test'
    expected_test_result = 230
    instance = Solution(file)
    instance.run()
    if instance.solution != expected_test_result:
        print("TEST Failed, aborting")
    else:
        file = 'input'
        instance = Solution(file).run()


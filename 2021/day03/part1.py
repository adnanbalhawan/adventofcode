

file = open('input', 'r')
# file = open('dummyinput', 'r')
data = file.readlines()

positional_stats = []
gamma_rate_array = []
epsilon_rate_array = []

for entry in data:
    # print(entry)
    for char_index in range(len(entry)):
        if entry[char_index] != '\n':
            try:
                positional_stats[char_index][int(entry[char_index])] += 1
            except IndexError as e:
                positional_stats.append([0, 0])
                positional_stats[char_index][int(entry[char_index])] += 1
            # print(char_index, entry[char_index], positional_stats[char_index], positional_stats)

gamma_rate = 0
epsilon_rate = 0

print(positional_stats)

for position_index_array in range(len(positional_stats)):   
    try: 
        if positional_stats[position_index_array][1] > positional_stats[position_index_array][0]:
            gamma_rate_array[position_index_array] = '1'
            epsilon_rate_array[position_index_array] = '0'
        else:
            gamma_rate_array[position_index_array] = '0'
            epsilon_rate_array[position_index_array] = '1'
    except IndexError:
        gamma_rate_array.append(None)
        epsilon_rate_array.append(None)
        if positional_stats[position_index_array][1] > positional_stats[position_index_array][0]:
            gamma_rate_array[position_index_array] = '1'
            epsilon_rate_array[position_index_array] = '0'
        else:
            gamma_rate_array[position_index_array] = '0'
            epsilon_rate_array[position_index_array] = '1'


print(gamma_rate_array)
print(epsilon_rate_array)

temp =''
gamma_rate = int(temp.join(gamma_rate_array), 2)
epsilon_rate = int(temp.join(epsilon_rate_array), 2)

print(gamma_rate, epsilon_rate, gamma_rate * epsilon_rate)

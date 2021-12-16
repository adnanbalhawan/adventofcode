
file = open('input', 'r')
# file = open('dummyinput', 'r')
data = file.readlines()
h_position = 0
depth = 0
aim = 0

for entry in data:        
    datapoint = entry.split()
    
    print(datapoint)
    
    instruction = datapoint[0]
    value = int(datapoint[1])

    if instruction == 'forward': 
        h_position += value
        depth += aim * value
    if instruction == 'up': aim -= value
    if instruction == 'down': aim += value

    print(f'aim: {aim}, h_position: {h_position}, depth: {depth}')

print(h_position * depth)
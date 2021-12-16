

file = open('input', 'r')
data = file.readlines()
h_position = 0
depth = 0

for entry in data:        
    datapoint = entry.split()
    
    print(datapoint)
    
    instruction = datapoint[0]
    value = int(datapoint[1])

    if instruction == 'forward': h_position += value
    if instruction == 'up': depth -= value
    if instruction == 'down': depth += value

print(h_position * depth)
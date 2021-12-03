
file = open('input', 'r')
data = file.readlines()

window_size = 3
count = 0 

for i in range(len(data)):
    if len(data[i:i+window_size]) == 3 and len(data[i+1:i+1+window_size]):
        first_sum = 0
        for item in data[i:i+window_size]:
            first_sum += int(item)
        
        secondary_sum = 0
        for item in data[i+1:i+1+window_size]:
            secondary_sum += int(item)
        
        if secondary_sum > first_sum:
            count += 1

        print(first_sum, secondary_sum, count)

print(count)

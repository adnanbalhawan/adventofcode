file = open('input', 'r')

prev_line = None
count = 0
for line in file:
    if prev_line is not None and int(line) > int(prev_line):
        count += 1
    prev_line = line

print(count)
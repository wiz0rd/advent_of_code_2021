import time
from collections import OrderedDict


input = OrderedDict()

iterator = 0
with open('input.txt', 'r') as f:
    for line in f:
        modified_line = []
        line = line.strip()
        for number in line:
            modified_line.append(int(number))
        input[iterator] = modified_line
        iterator += 1

line_length = (len(input[0]) - 1)
dict_length = (len(input) - 1)
#rint(dict_length)
#print(line_length)

basins = {}

dict_tracker = 0
for k in input.keys():
    index_tracker = 0
    print(input[k])
    
    

import time
from collections import OrderedDict


final_list = []

#Make a list to store the input
original_input = []
#Open the input and append it to the list
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        original_input.append(line)
   
#Make an orderered dictionary called input_dict
input_dict = OrderedDict()

#calculate the line length of each line to start and make two lines to be used for line 0 and the last line
line_length = len(original_input[0])


make_first_entry = []
make_last_entry = []
for number in range(line_length + 2):
    make_first_entry.append(99)
    make_last_entry.append(99)

#Code to modify the list from strings to integer and to add the modified lists to the ordered dict
dict_iterator = 1
for line in original_input:
    modified_list = []
    for string in line:
        modified_list.append(int(string))
    input_dict[dict_iterator] = modified_list
    dict_iterator += 1

#Code to add values to the beginning and end of each line
for k in input_dict.keys():
    input_dict[k].insert(0, 99)
    input_dict[k].append(99)

#Code to add the first line and last line to the list
input_dict[0] = make_first_entry
input_dict[len(input_dict)] = make_last_entry
dict_tracker = 1
for k in sorted(input_dict.keys()):
    num_tracker = 1
    
    if input_dict[k][5] == 99:
        continue
      
    else:
        
        print(input_dict[k][1:11])
        for number in input_dict[k][1:101]:
            
            if number < input_dict[k][num_tracker + 1]:
                
                if number < input_dict[k][num_tracker - 1]:
                    
                    if number < input_dict[dict_tracker - 1][num_tracker]:
                        if number < input_dict[dict_tracker + 1][num_tracker]:
                            final_list.append(number)
                num_tracker += 1
            else:
                num_tracker += 1
    dict_tracker += 1
print(final_list)

high_score = 0
for number in final_list:
    high_score += (number + 1)
    
print(high_score)
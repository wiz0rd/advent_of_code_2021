import time
from multiprocessing import Pool

line_zero = 0

rules = {}
#read in the file
with open('input.txt', 'r') as f:
    for line in f:
    
        if line_zero == 0:
            starting_point = line.strip()
            line_zero += 1
        elif '->' in line:
             line = line.strip().split()
             rules[line[0]] = line[2]

#define a list of letters in the starting polymer for use with scoring
letters = []
for letter in starting_point:
    if letter not in letters:
        letters.append(letter)

#make the starting polymer
current_polymer = list(starting_point)

#create the function to make the new polymers
def find_current_pairs_and_insert_element(x):
    global current_polymer
    current_polymer = list(current_polymer)
    copy_polymer = current_polymer.copy()
    current_pairs = []
    number_of_pairs = len(current_polymer) - 1
    for pair in range(number_of_pairs):
        pop = copy_polymer.pop(0)
        pull = copy_polymer[0]
        current_pairs.append(pop + pull)
    final_tris = []
    new_tris = []
    for pair in current_pairs:
        if pair in rules:
            tri_start = list(pair)
            tri_start.insert(1, rules[pair])
            new_tris.append(''.join(tri_start))
    tri_len = len(new_tris) - 2
    for tri in new_tris[:-1]:
        tri_list = list(tri)
        tri_list.pop()
        final_tris.append(''.join(tri_list))
    final_tris.append(new_tris[-1])
    
    current_polymer = ''.join(final_tris)
    return ''.join(final_tris)

#run the function 40 times

#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#print('10 rounds complete')
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#print('20 rounds complete')
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#print('30 rounds complete')
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#print('35 rounds complete')
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#print('38 rounds complete')
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)
#time.sleep(0.5)
#current_polymer = list(find_current_pairs_and_insert_element())
#print(current_polymer)

#pool = Pool(processes=8)
#m = 10
#pool.map(find_current_pairs_and_insert_element, range(m))

for number in range(20):
    #print(current_polymer)
    find_current_pairs_and_insert_element(1)
    print(number)
    #print(current_polymer)


#define a dictionary for a score list and show the number of occurances for each letter defined in the letters list
score_list = {}
for letter in letters:
    score_list[letter] = current_polymer.count(letter)
#print(score_list)

high_score = 0
low_score = 9999999999999999
for v in score_list.values():
    if v > high_score:
        high_score = v
    elif v < low_score:
        low_score = v

print(high_score)
print(low_score)
print('ANSWER:')
print(high_score - low_score)
from sympy import symbols, solve, Eq
import time

starting_positions = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        for value in line:
            starting_positions.append(int(value))

def get_fuel_cost(num, targ):
    fuel_cost = 0
    base_value = abs(num - targ)
    #print(base_value)
    for number in range(1, base_value + 1):
        #print(number)
        fuel_cost += number
    return fuel_cost

min_position = min(starting_positions)
max_position = max(starting_positions)
print(min_position)
print(max_position)

incrementor = 0
current_low_scorer = 'placeholder'
current_low_score = 9999999999999999999999999999999999999999999999999999
current_value = 0
results = []
for number in range(min_position, max_position):
    
    current_score = 0
    for value in starting_positions:

        current_score += get_fuel_cost(value, number)
    
    if current_score < current_low_score:
        current_low_scorer = number
        current_low_score = current_score

print(current_low_scorer)
print(current_low_score)

    
        


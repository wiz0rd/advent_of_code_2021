
### "acc" increases or decreases a single global value called the accumulator by the
### value given in the argument. For example, acc +7 would increase the accumulator
### by 7. The accumulator starts at 0. After an acc instruction, the instruction
### immediately below it is executed next.

### "jmp" jumps to a new instruction relative to itself. The next instruction 
### to execute is found using the argument as an offset from the jmp instruction;
### for example, jmp +2 would skip the next instruction, jmp +1 would continue to
### the instruction immediately below it, and jmp -20 would cause the instruction
###  20 lines above to be executed next.

### "nop" stands for No OPeration - it does nothing. The instruction immediately
###  below it is executed next.

from collections import OrderedDict
iterator = 0
moves = OrderedDict()
moves = {}
accumulator = 0
with open('/home/juicy_joshy/Documents/advent_of_code/advent_day_8_a.txt', 'r') as f:
    for line in f:
        line = line.strip().split()
        moves[iterator] = line
        iterator += 1

moves_used = []
current_move = 0
while current_move not in moves_used:
    moves_used.append(current_move)
    if moves[current_move][0] == 'acc':
        move_value = moves[current_move][1]
        move_value = list(move_value)
        operator = move_value[0]
        move_value = ''.join(move_value[1:])
        move_value = int(move_value)
        if operator == '+':
            accumulator += move_value
        elif operator == '-':
            accumulator -= move_value
        current_move += 1
    elif moves[current_move][0] == 'jmp':
        move_value = moves[current_move][1]
        move_value = list(move_value)
        operator = move_value[0]
        move_value = ''.join(move_value[1:])
        move_value = int(move_value)
        if operator == '+':
            current_move += move_value
        elif operator == '-':
            current_move -= move_value
    elif moves[current_move][0] == 'nop':
        current_move += 1
print(accumulator)

print(moves_used)

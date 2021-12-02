current_position = {
    'horizontal': 0,
    'vertical': 0,
}



moves = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        moves.append(line)
for move in moves:
    move = move.split()
    if move[0] == 'forward':
        current_position['horizontal'] += int(move[1])
    
    elif move[0] == 'up':
        current_position['vertical'] -= int(move[1])

    elif move[0] == 'down':
        current_position['vertical'] += int(move[1])

for k,v in current_position.items():
    print(k + ' ' + str(v))

print('answer: ' + str(2034 * 702))
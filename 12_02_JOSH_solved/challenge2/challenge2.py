current_positions = {
    'aim': 0,
    'depth': 0,
    'horizontal': 0,
}

moves = []
with open('input.txt', 'r') as f:
    for line in f:
        moves.append(line.strip())

for move in moves:
    move = move.split() #splits into move[0] (direction) and move[1] the value
    if move[0] == 'down':
        current_positions['aim'] += int(move[1]) #move[1] is the numerical move value
    elif move[0] == 'up':
        current_positions['aim'] -= int(move[1]) #move[1] is the numerical move value
    elif move[0] == 'forward':
        current_positions['horizontal'] += int(move[1]) #move[1] is the numerical move value
        current_positions['depth'] += (current_positions['aim'] * int(move[1]))
    
for k, v in current_positions.items():
    print(k + ' : ' + str(v))

print('final answer:' + str(2034 * 770963))
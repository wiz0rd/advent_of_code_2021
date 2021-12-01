lines = []
increased = []
decreased = []

with open("input.txt") as f:
    read_lines = f.readlines()
    for i in read_lines:
        i = i.strip()
        i = int(i)
        lines.append(i)

for pre, cur in zip(lines, lines[1:]):
    # print(pre, cur)
    if cur > pre:
        # print('increased')
        increased.append(cur)
    else:
        # print('decreased')
        decreased.append(cur)
print(f"the answer is {len(increased)}")

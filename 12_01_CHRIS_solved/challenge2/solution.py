lines = []
increased = []
decreased = []

with open("input.txt") as f:
    read_lines = f.readlines()
    for i in read_lines:
        i = i.strip()
        i = int(i)
        lines.append(i)

window_size = 3
totals = []
for i in range(len(lines) - window_size + 1):
    batch = lines[i : i + window_size]
    # print(batch)
    window_total = sum(batch)
    # print(window_total)
    totals.append(window_total)

increased_2 = []
decreased_2 = []

for pre, cur in zip(totals, totals[1:]):
    # print(pre, cur)
    if int(cur) > int(pre):
        # print('increased')
        increased_2.append(cur)
    else:
        # print('decreased')
        decreased_2.append(cur)
print(f"the answer is {len(increased_2)}")

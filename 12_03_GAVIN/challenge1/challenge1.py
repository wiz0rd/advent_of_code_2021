

with open("input.txt") as f:
    binary = f.readlines()

most = len(binary)/2
count = []
for _ in range(len(binary[0])-1):
    count.append(0)

for w in binary:
    for b in range(len(w)-1):
        if w[b] == '1':
            count[b] += 1

gamma = ""
for c in count:
    if c >= most:
        gamma += "1"
    else:
        gamma += "0"

epsilon = ""
for c in gamma:
    if c == "1":
        epsilon += "0"
    else:
        epsilon += "1"

print(int(gamma,2) * int(epsilon,2))
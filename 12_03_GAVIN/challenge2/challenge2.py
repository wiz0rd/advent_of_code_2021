

with open("input.txt") as f:
    binary = f.read().splitlines()

def oxygenfilter(data, bit):
    count = 0
    most = len(data)/2
    ones = []
    zeros = []
    for w in data:
        if w[bit] == "1":
            count += 1
            ones.append(w)
        else:
            zeros.append(w)
    if count >= most:
        return ones
    else:
        return zeros

def co2filter(data, bit):
    count = 0
    most = len(data)/2
    ones = []
    zeros = []
    for w in data:
        if w[bit] == "0":
            count += 1
            zeros.append(w)
        else:
            ones.append(w)
    if count <= most:
        return zeros
    else:
        return ones

i = 0
oxygen = binary
while len(oxygen) != 1:
    oxygen = oxygenfilter(oxygen,i)
    i += 1

i = 0
co2 = binary
while len(co2) != 1:
    #print(co2)
    co2 = co2filter(co2,i)
    i+= 1

print(oxygen)
print(co2)
print(int(oxygen[0],2) * int(co2[0],2))
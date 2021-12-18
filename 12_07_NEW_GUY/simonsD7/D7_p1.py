import statistics as stat

with open('D7/D7inp.txt') as inp:
    inpread = inp.readlines()

holder = []
for x in inpread[0].split(','):
    holder.append(int(x))

moveTo = (int(stat.median(holder)))

def fuel(positions, mV):
    fuel = 0
    for x in positions:
        if x <= mV:
            temp = mV - x
            fuel += temp
        else:
            temp = x - mV
            fuel += temp  
    return fuel

print (fuel(holder,moveTo))
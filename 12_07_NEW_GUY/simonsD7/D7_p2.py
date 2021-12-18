#95476248 too high

import statistics as stat

with open('D7/D7inp.txt') as inp:
    inpread = inp.readlines()

holder = []
for x in inpread[0].split(','):
    holder.append(int(x))

moveTo = round((stat.mean(holder)))

def fuel(positions, mV):
    fuel = 0
    for x in positions:
        if x <= mV:
            temp = mV - x
            fuel += (temp*(temp+1))/2
        else:
            temp = x - mV
            fuel += (temp*(temp+1))/2 
    return fuel

#print(holder)
#print(fuel(holder,moveTo))

holder2 = []
x = moveTo - 50
while x < moveTo + 50:
    holder2.append(fuel(holder,x))
    x += 1

print(min(holder2))
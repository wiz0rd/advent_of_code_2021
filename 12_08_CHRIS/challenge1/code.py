#! /usr/bin/env python

from aocd import get_data

test = get_data(day=8, year=2021).splitlines()

counter = 0

for i in test:
    tail = i.split("|", 1)[1]
    tail_grp = tail.split()
    for i in tail_grp:
        # if len(i) == 2:
        #     print("found a number one")
        #     counter += 1
        # elif len(i) == 3:
        #     print("found a number seven")
        #     counter += 1
        # elif len(i) == 4:
        #     print("found a number four")
        #     counter += 1
        # elif len(i) == 7:
        #     print("found a number eight")
        #     counter += 1
        # if len(i) == 2 or len(i) == 3 or len(i) == 4 or len(i) == 7:
        if len(i) in (2, 3, 4, 7):
            print("found a number")
            counter += 1
        else:
            print(i)

print(f"found {counter} possible numbers....")

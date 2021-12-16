#! /usr/bin/env python

from aocd import get_data

test = get_data(day=8, year=2021).splitlines()

# acedgfb = 8
# cdfbe = 5
# gcdfa = 2
# fbcad = 3
# dab = 7
# cefabd = 9
# cdfgeb = 6
# eafb = 4
# cagedb = 0
# ab = 1

# dict = {
#     "0": cagedb,
#     "1": ab,
#     "2": gcdfa,
#     "3": fbcad,
#     "4": eafb,
#     "5": cdfbe,
#     "6": cdfgeb,
#     "7": dab,
#     "8": acedgfb,
#     "9": cefabd,
# }

dict2 = {
    "0": "abcdeg",
    "1": "ab",
    "2": "acdfg",
    "3": "abcdf",
    "4": "abef",
    "5": "bcdef",
    "6": "bcdefg",
    "7": "abd",
    "8": "abcdefg",
    "9": "abcdef",
}

for i in test:
    tail = i.split("|", 1)[1]
    print(f"..............{tail}")
    tail_grp = tail.split()
    tail_grp_string = []
    for i in tail_grp:
        alph = "".join(sorted(i))
        print(f"{alph}     gibberish:{i}")
        # print(list(dict2.keys())[list(dict2.values()).index(i.join(sorted(i)))])
        # tail_grp_string.append(str(i))
    print(tail_grp_string)
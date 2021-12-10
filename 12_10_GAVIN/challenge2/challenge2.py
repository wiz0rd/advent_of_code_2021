
scores = []
points = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

with open("input.txt","r") as f:
    for lines in f:
        line = lines.strip()
        match = []
        corrupt = False
        for char in line:
            if char == "(":
                match.append(")")
            elif char == "[":
                match.append("]")
            elif char == "{":
                match.append("}")
            elif char == "<":
                match.append(">")
            elif char != match[-1]:
                corrupt = True
                break
            else:
                match = match[:-1]
        if corrupt == False:
            s = 0
            #print(match)
            for m in reversed(match):
                #print(f"{s} * 5 + {points[m]}")
                s = (s * 5) + points[m]
                #print(f"new totol s = {s}")
            scores.append(s)

        
scores.sort()
print(scores[int(len(scores)/2)])
# 3103006161
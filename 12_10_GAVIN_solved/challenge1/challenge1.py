
score = 0
points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

with open("input.txt","r") as f:
    for lines in f:
        line = lines.strip()
        match = []
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
                #print(f"illegal = {char}, worth {points[char]}")
                score += points[char]
                break
            else:
                match = match[:-1]

print(score)
# 323613
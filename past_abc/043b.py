S = list(input())
result = []
for s in S:
    if s != "B":
        result.append(s)
    elif len(result) == 0:
        continue
    else:
        result.pop()

print("".join(result))
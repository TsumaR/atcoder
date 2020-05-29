S = input()
ans = 0
count = [0] * len(S)
tmp = 0
for i in reversed(range(len(S))):
    if S[i] == "B":
        count[i] = tmp
    else:
        tmp += 1

print(sum(count))

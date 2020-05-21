S = list(input())
T = int(input())

x = 0
y = 0
z = 0

for s in S:
    if s == "L":
        x -= 1
    elif s == "R":
        x += 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    else:
        z += 1

if T == 1:
    print(abs(x)+abs(y) + z)
else:
    print(max(abs(x) + abs(y) - z, len(S)%2))
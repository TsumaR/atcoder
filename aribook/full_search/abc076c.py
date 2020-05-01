import sys

S = list(input())
T = list(input())

length = len(T)
position = len(S) - length

while position >= 0:
    text = S[position:position+length]
    for i in range(length):
        if text[i] == "?":
            text[i] = T[i]
    if text != T:
        position -= 1
    else:
        S[position:position+length] = T
        position = -10

if position != -10:
    print("UNRESTORABLE")
    sys.exit()

for i in range(len(S)):
    if S[i] == "?":
        S[i] = "a"

print("".join(S))




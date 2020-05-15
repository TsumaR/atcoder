"""
３回以上かかることはない
"""

S = list(input())
l = len(S)
count = 0
for i in range(l):
    if S[i] == "U":
        count += l-1-i
        count += 2*i
    else:
        count += (l-1-i)*2
        count += i

print(count)

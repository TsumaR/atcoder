import collections
n=int(input())
l=[input() for i in range(n)]

c = collections.Counter(l)

print(len(c))
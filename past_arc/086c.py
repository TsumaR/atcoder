from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

C = list(Counter(A).most_common())
count = 0
while len(C) > K:
    tmp = C.pop()
    count += tmp[1]
print(count)

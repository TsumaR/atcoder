from collections import deque

N = int(input())

A = deque(range(1,10))

count = 0
for _ in range(N):
    k = A.popleft()
    m = k % 10
    if m != 0:
        A.append(10 * k + m -1)
    A.append(10 * k + m)
    if m != 9:
        A.append(10 * k + m + 1)
print(k)
    
N = int(input())
A = [0] + list(map(int, input().split())) + [0]

dist = []
for i in range(1, len(A)):
    dist.append(abs(A[i] - A[i-1]))

total = sum(dist)

for i in range(N):
    a = total - dist[i] - dist[i+1]
    a += abs(A[i] - A[i+2])
    print(a)
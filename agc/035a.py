
N = int(input())
A = list(map(int, input().split()))
b = 0

for i in range(N):
    b ^= A[i]

print("Yes" if b == 0 else "No")
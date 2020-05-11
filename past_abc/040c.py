N = int(input())
A = list(map(int, input().split()))

R = [0] * N
R[1] = abs(A[1] - A[0])

for i in range(2,N):
    R[i] = min(R[i-2] + abs(A[i] - A[i-2]), R[i-1] + abs(A[i] - A[i-1]))

print(R[N-1])
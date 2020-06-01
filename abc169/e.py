N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

A.sort()
B.sort()

if N % 2 == 1:
    mid = N // 2
    print(B[mid] - A[mid] +1)
else:
    mid1 = N // 2
    mid2 = mid1 -1
    smallest = A[mid1] + A[mid2]
    largest = B[mid1] + B[mid2]
    print(largest - smallest + 1)

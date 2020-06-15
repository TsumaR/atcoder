import heapq
N = int(input())
A = list(map(int, input().split()))

A = list(set(A))
if len(A) == 1:
    print(0)
    exit()
A.sort()
count = 0
divisor_list = []
while len(A) >= 1:
    B = []
    count += 1
    item = A[0]
    for j in list(A):
        if j % item != 0:
            B.append(j)
    A = B

print(count)
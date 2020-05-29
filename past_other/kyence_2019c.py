N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
else:
    minus_count = []
    plus_count = []
    for i in range(N):
        dist = A[i] - B[i]
        if dist > 0:
            plus_count.append(dist)
        elif dist < 0:
            minus_count.append(dist)
    plus_count.sort()
    minus_sum = sum(minus_count)
    count = len(minus_count)
    while minus_sum < 0:
        minus_sum += plus_count.pop()
        count += 1
    print(count)
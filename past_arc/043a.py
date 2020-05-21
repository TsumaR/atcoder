import statistics
N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]
max_point = max(S)
min_point = min(S)
mean_point = statistics.mean(S)

if max_point == min_point:
    print(-1)
    exit()
P = B / (max_point - min_point)
Q = A - P * mean_point
print(P, Q)
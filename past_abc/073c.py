N, T = map(int, input().split())
T_list = list(map(int, input().split()))

result = T
for i in range(1,N):
    result += min(T, T_list[i] - T_list[i-1])

print(result) 
N, K = map(int, input().split())
P = list(map(int, input().split()))

sum_ans = sum([(i+1)/2 for i in P[0:K]])
result = [sum_ans]
for i in range(K,N):
    result.append(result[-1] + (P[i]+1)/2 - (P[i-K]+1)/2)

print(max(result))
N = int(input())
S = list(input())

result = 0
for i in range(N):
    num = set(S[0:i+1]) & set(S[i+1:N])
    # print(num)
    result = max(result, len(num))
print(result)
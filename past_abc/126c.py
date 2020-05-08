# from math import ceil

# N, K = map(int, input().split())

# A = 1 / N
# temp = N
# count = 0
# while True:
#     if temp >= K:
#         break
#     temp *= 2
#     count += 1

# T = []
# T.append(count)
# C = 0

# for i in reversed(range(1, N)):
#     if i * (2 ** count) < K:
#         count +=1
#         T.append(count)
#     else:
#         T.append(count)

# ans = 0
# for i in T:
#     ans += A * (0.5 ** i)
# print(ans)

n,k = map(int,input().split())
p = 0
for i in range(1,n+1):
    x = 0
    while(i<k):
        i=i*2
        x+=1
    p+=(1/n)*((1/2)**x)
print(p)
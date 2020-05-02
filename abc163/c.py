import math

K = int(input())

dp = [[0] * 201 for _ in range(201)]

def dp_gcds(x,y):
    if dp[x][y] != 0:
        n = dp[x][y]
    else:
        n = math.gcd(x,y)
        dp[x][y] = n
        dp[y][x] = n
    return n
    
def gcds(x,y,z):
    n1 = dp_gcds(x,y)
    n2 = dp_gcds(n1,z)
    return n2

total = 0
for i in range(1,K+1):
    for j in range(1, K+1):
        for t in range(1, K+1):
            total += gcds(i,j,t)
print(total)
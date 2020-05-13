N = int(input())
# 素数の登場回数を記録する
ps = [0] * (N+1)

for i in range(2,N+1):
  x = i
  p = 2
  while x > 1 :
    while x % p == 0:
      ps[p] += 1
      x //= p
    p += 1
ans = 1
for c in ps:
  ans = (ans * (c+1)) % 1000000007
print(ans)
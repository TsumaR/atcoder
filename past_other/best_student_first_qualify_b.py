N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7
result = 0
count = [0] * 2001

# リスト内での繰り返し
for a in A:
    count[a-1] += 1
    result += K * sum(count[a:])
    result %= mod

kn = 0
# 前のループに存在する自分より大きい数
count = [i for i in count if i != 0]
total = sum(count) % mod

for i in count:
    total -= i
    kn += total * i
    kn %= mod

result += kn * K*(K-1)//2
result %= 10**9 + 7

print(result)

N, K = map(int, input().split())
A = list(map(int, input().split()))

"""
1からのループだけを考えれば良い
"""

i = A[0]
ok = True
R = [1]
seen = [0] * N
seen[0] = 1
count = 1

# ずっとエラーだったのは，1から出て1に戻るのがexceptionされていた
if A[0] == 1:
    print(1)
    exit()

while ok:
    count += 1
    seen[i-1] += count
    R.append(i)
    i = A[i-1]
    # 訪れたことがあれば
    if seen[i-1] != 0:
        k = seen[i-1]
        loop = R[k-1:]
        remain = R[:k-1]
        ok = False

L = len(loop)

if K < len(remain):
    print(remain[K])
else:
    print(loop[(K - len(remain)) % L])

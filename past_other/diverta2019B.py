R, G, B, N = map(int, input().split())
"""
3000以下なので全探索を考える。
まず，全探索できるものは全探索から考える必要がある。
オーダーを計算し，いけそうならそれで行くべき。今回は固定を順にしていくので間に合う
そこから探索する範囲を絞り込んで
"""

count = 0
for r in range(N//R+1):
    rest = N - r*R
    for g in range(rest//G+1):
        n_b = (rest - g*G)
        if n_b % B == 0 and n_b >= 0:
            count += 1
print(count)
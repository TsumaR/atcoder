import itertools
N = int(input())
C = list(input())
C.append("ZZ")

"""
二文字をショートカット
長さは1000以下
ショートカットの組み合わせは合計で16通り
全てに対して試して，登場回数の多い二つをとる（二つをとっていけるかは微妙，全探索する必要があるかもしれない）

最初に考えたやり方と一緒。
"""

def F(L, R):
    cnt = 0 # 短縮成功回数をいれる
    i = 0
    while i < N:
        # i文字目
        if C[i] == L[0] and C[i+1] == L[1]:
            cnt += 1
            i += 2
        elif C[i] == R[0] and C[i+1] == R[1]:
            cnt += 1
            i += 2
        else:
            i += 1
        continue
    return N - cnt

answer = N
se = set(itertools.product('ABXY', repeat = 2))
for L,R in itertools.combinations(se,2):
  answer = min(answer, F(L,R))
print(answer)
import copy

n, m, q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(q)]

B = []

# 一列の玉を，仕切り板によって分ける問題だと考えれば良い
# 全ての並び方の候補を全探索する。
# 再帰を用いる。

# 深さ優先探索で再帰を当たり前に使えるようにならないといけない。

# 各ボールがどこに入っているかの候補リストを出す再帰関数
# 例えば最初の例題の答えの物は，全ての結果の中から[1, 3, 4]というものを選んだことになる。
def dfs(A, l):
    if l == n:
        # 長さが，Nになったときにのみ，Bというグローバル変数に代入する。
        B.append(A)
    else:
        # ボールを，入る箇所でラベルしながら加えていく。forで回す。
        # ただし，入る箇所は前のものと同じかそれより後ろにならないといけなのでrangeに注意
        for i in range(A[-1], m+1):
            nA = copy.copy(A)
            nA.append(i)
            dfs(nA, l+1)
dfs([1],1)


# ここまでで，ありうる全ての候補が上がった。
ans = 0
for ls in B:
    point = 0
    for que in Q:

        if ls[que[1]-1] - ls[que[0]-1] == que[2]:
            point += que[3]
    ans = max(point, ans)

print(ans)
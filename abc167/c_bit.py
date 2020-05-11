N, M, X = map(int, input().split())
C = []; A = []; T = []
for _ in range(N):
    s = list(map(int, input().split()))
    C.append(s[0])
    A.append(s[1:])

INF = 10**9
ans = INF
# シフトで2^nまで全探索
# 全ての組み合わせに対してforを回す
# 部分集合を全探索するならbit全探索
# 左シフト<< 桁を左にずらし，0を入れていく
for s in range(0, 1 << N):
    # 習得度をいれるリストを定義
    smart = [0] * M
    cost_sum = 0
    # sには一旦10進数が入る
    # 得られた１組あわせに対して，2進数でそのitemを用いているかを (s >> i) & 1で確認する
    # これは，右シフト
    # 012のループ
    for i in range(N):
        # 買っているかを
        if (s >> i) & 1:
            cost_sum += C[i]
            for j in range(M):
                smart[j] += A[i][j]
    ok = True
    if min(smart) < X:
        ok = False
    if ok:
        ans = min(ans, cost_sum)

if ans == INF:
    print(-1)
else:
    print(ans)
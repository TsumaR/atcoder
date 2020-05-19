from collections import Counter

N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

ans = 1
cnt = 0
# 最後にバスが出た時間
st = T[0]
for t in T:
    cnt += 1
    # バスが出てからK時間以上たつ or count が　C を越した場合
    if t - st > K or cnt > C:
        ans += 1
        st = t
        cnt = 1

print(ans)
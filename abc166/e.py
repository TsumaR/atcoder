# 常にi < jを考える
from collections import Counter

N = int(input())
H = [0]
H.extend(list(map(int, input().split())))

plus = [H[i] + i for i in range(1,N+1)]
minus = [i - H[i] for i in range(1, N+1)]
ans = 0

# 独立というのがよくわからなかったが，
# i > jで成り立つと仮定すると，
# aj -ai = Ai + Aj > 0　で，
# j > i となり，矛盾する。
# 連想配列で調べれば良い

cnt = Counter(minus)

for i in plus:
    ans += cnt.get(i, 0)

print(ans)
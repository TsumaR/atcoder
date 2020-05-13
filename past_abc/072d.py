"""
思考
N <= 10 ** 5
O(N)は通る

すでにpi != iのところは置き換えたくない
隣同士しか変えられない

隣もpi == iだったら喜んで変える
基本的に後ろのやつと変えると固定

最後が残るのくらい気づけないとまずいと思う
"""

N = int(input())
P = list(map(int, input().split( )))

count = 0
for i in range(len(P) - 1):
    if i + 1 != P[i]:
        continue
    else:
        P_temp = P[i]
        P[i] = P[i + 1]
        P[i + 1] = P_temp
        count += 1

if N == P[N-1]:
    print(count + 1)
    exit()

print(count)
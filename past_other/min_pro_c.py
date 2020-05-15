K, A, B = map(int, input().split())

if A + 2 >= B:
    print(1 + K)
    exit()

# ループに入るまでの操作
count = A
K -= (A - 1)
# これ以降はAを交換してBを繰り返す。２回ごとにBーA増えていく

count += (K // 2) * (B - A)
# B変換できない分のあまりは叩いて増やしておく
count += K % 2
print(count)
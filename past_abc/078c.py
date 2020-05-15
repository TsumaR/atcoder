N, M = map(int, input().split())
count = 0

longs = M * 1900
short = (N-M) * 100
time = longs + short

prob = 2**M
# 無限級数和を考えて
print(time * prob)
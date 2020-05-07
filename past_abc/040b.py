# h >= wで固定
import math
N = int(input())
sq = int(math.sqrt(N))
 
minimum = 1000000
for h in range(1, N+1):
    minimum = min(minimum, abs(h - N//h) + N%h)
 
print(minimum)
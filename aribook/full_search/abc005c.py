import copy
import sys
from collections import deque

# 何秒以内のたこ焼きまで売るか
T = int(input())
# たこ焼きの数
N = int(input())
A = list(map(int, input().split()))
# 来店者数
M = int(input())
B = list(map(int, input().split()))

# 客と
takoyaki = [0] * 100
customer = [0] * 100

for i in A:
    takoyaki[i] += 1
for i in B:
    customer[i] += 1

# メイン
yakiagari = deque([])
for i in range(100):
    for _ in range(takoyaki[i]):
        yakiagari.append(T)
    if len(yakiagari) < customer[i]:
        print("no")
        sys.exit()
    else:
        for _ in range(customer[i]):
            yakiagari.popleft()
    yakiagari = map(lambda x: x-1, yakiagari)
    yakiagari = deque([l for l in yakiagari if l < 0])
    
print("yes")
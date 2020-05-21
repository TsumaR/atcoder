from statistics import mean
import math

N = int(input())
A = list(map(int, input().split()))

mean_num = mean(A)
Ceil = math.ceil(mean_num)
Floor = math.floor(mean_num)

Ceil_sum = 0
Floor_sum = 0
for i in A:
    Ceil_sum += (Ceil - i) ** 2
for i in A:
    Floor_sum += (Floor - i) ** 2

print(min(Floor_sum, Ceil_sum))
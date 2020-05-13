"""
マスターオブ整数，素数
約数の総和
"""

"""
約数列挙の回答
"""

N = int(input())
if N == 1:
    print("Deficient")
    exit()

divisor = []
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        if i != N//i:
            divisor.append(i)
            divisor.append(N//i)
        else:
            divisor.append(i)

sum_div = sum(divisor) + 1
if sum_div == N:
    print("Perfect")
elif sum_div < N:
    print("Deficient")
else:
    print("Abundant")
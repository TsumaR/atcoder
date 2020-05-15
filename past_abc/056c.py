"""
異なる数の足し算で
行ける最大の距離を一秒ずつ算出し，こした時がその値
つまり，そこまでの内で一つを除けば辿りつくはず

数列の和を求めていく
"""

X = int(input())
count = 0
ans = 0
for i in range(1,X+1):
    count += i
    ans += 1
    if count >= X:
        print(ans)
        exit()
# 奇数の時
# a，b，cはkの倍数
# kが偶数
# a, b, cがkの倍数
#　もしくは，全てk/2の倍数

N, K = map(int, input().split())

if K % 2 != 0:
    n = N // K 
    print(n ** 3)

else:
    n = N // K
    half_n = N // (K//2)
    print(n ** 3 + (half_n - n)** 3)
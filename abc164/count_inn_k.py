"""
n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 AA が与えられる。
これらの整数から K 個以内の整数を選んで総和が A になるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

【制約】
・1≤K≤n≤5001≤K≤n≤500
・1≤a[i]≤10001≤a[i]≤1000
・1≤A≤100001≤A≤10000
"""

n = int(input())
a = list(map(int, input()))
A = int(input())
K = int(input())

# 実装はcount_num_min.pyと一緒


"""
N <= 100
h <= 100
ということで,実装さえすれば通りそう
山の絵を書いて考える
"""

N = int(input())
H = [-1] + list(map(int, input().split()))

ans = 0
for _ in range(max(H)):
    count = 0
    for j in range(N):
        if H[j] <= 0 and H[j+1] > 0:
            count += 1
    ans += count
    H = [i-1 for i in H]
    print(H)
    print(ans)
        
print(ans)
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 1
N -= K
count += N //(K-1)
if N % (K-1)== 0:
    print(count)
    exit()

print(count+1)
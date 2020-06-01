N = int(input())
X = list(map(int, input().split()))
start = min(X)
stop = max(X)
count = 0 
ans = 10**10
for i in range(start, stop+1):
    count = 0
    for x in X:
        count += (x-i)**2
    ans = min(count, ans)
print(ans)
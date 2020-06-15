import heapq

N = int(input())
A = list(map(int, input().split()))

heapq.heapify(A)
if len(set(A)) == 1:
    print(0)
    exit()
count = 0
divisor_list = []
for _ in range(N):
    ans = True
    item = heapq.heappop(A)
    for j in divisor_list:
        if item % j == 0:
            ans = False
            break
    if ans == True:
        count += 1
    divisor_list.append(item)

print(count)
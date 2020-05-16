from collections import deque

K = int(input())
que = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

count = 0
while True:
    n = que.popleft()
    count += 1
    if count == K:
        print(n)
        exit()
    if 1 <= n%10 <= 8: 
        que.append(n*10 + n%10 - 1)
        que.append(n*10 + n%10)
        que.append(n*10 + n%10 + 1)
    elif n%10 == 0:
        que.append(n*10 + n%10)
        que.append(n*10 + n%10 + 1)
    else:
        que.append(n*10 + n%10 - 1)
        que.append(n*10 + n%10)
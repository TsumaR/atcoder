N, A, B = map(int, input().split())
min_num = A*(N-1) + B
max_num = B*(N-1) + A

if max_num - min_num + 1 >= 0:
    print(max_num - min_num + 1)
else:
    print(0)
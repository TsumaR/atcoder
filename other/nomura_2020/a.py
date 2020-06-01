sh, sm, eh, em, K = map(int, input().split())

time = 60*(eh-sh) + em - sm
print(time - K)
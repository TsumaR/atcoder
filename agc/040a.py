s = input()
partition = s.replace('><','>|<').split('|')
ans=0

for sub in partition:
    left = sub.count('<')
    right = sub.count('>')
    ans += sum(range(1, max(left, right) + 1))
    ans += sum(range(1, min(left, right)))

print(ans)
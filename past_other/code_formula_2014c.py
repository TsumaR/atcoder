S = list(input().split(' '))

user_list = []
for s in S:
    l = len(s)
    for i in reversed(range(len(s[::-1]))):
        if s[i] == '@':
            user_list.append(s[i+1:l])
            l = i

user_set = set(user_list)
if "" in user_set:
    user_set.remove("")
user = sorted(list(user_set))
for s in user:
    print(s)
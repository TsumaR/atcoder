N = int(input())
count = 0
item = [3, 5, 7]

def dfs(s):
    global count
    if s > N:
        return
    string = str(s)
    if '3' in string and '5' in string and '7' in string:
        count += 1
    dfs(10*s + 3)
    dfs(10*s + 5)
    dfs(10*s + 7)

dfs(0)
print(count)
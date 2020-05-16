x, y = map(int, input().split())
count = abs(abs(x) - abs(y))

if x*y >= 0 and y > x:
    print(y - x)
elif x*y >= 0: # 符号同じなのにxの方が大きい場合のみ，入れ替えてから足して行き，もう一度入れ替える必要がある
    print(count+2)
else:
    print(count+1)


"""
普通こうするらしい，確かに。。。

x, y = map(int, input().split())
 
def f(x):
    if x<0:
        return 10**10
    else:
        return x
ans = min(f(y-x), f(y+x)+1, f(-y-x)+1, f(-y+x)+2)
print(ans)
"""
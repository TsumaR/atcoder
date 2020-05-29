s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
S = "".join(s)
T = "".join(t)
st = [S, T]
st.sort()

if S == T:
    print("No")
elif st[0] == S:
    print("Yes")
else:
    print("No")
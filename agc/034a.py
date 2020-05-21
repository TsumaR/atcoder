N, A, B, C, D = map(int ,input().split())
S = list(input())

"""
基本的にはシャープが2連続するとだめ
ただし，片方が間に必ず入っている場合は，...が三連続するところがないとダメ
"""

if A<B and C>D:
    for i in range(B-2,D-1):
        if S[i:i+3] == [".", ".", "."]:
            print("Yes")
            exit()
    print("No")
    exit()
elif A>B and C<D:
    for i in range(A-2,C-1):
        if S[i:i+3] == [".", ".", "."]:
            print("Yes")
            exit()
    print("No")
    exit()
else:
    for i in range(min(A,B)-1, max(C,D)-1):
        if S[i] == S[i+1] == "#":
            print("No")
            exit()
print("Yes")
N = int(input())
A = list(map(int, input().split()))

count = 1
state = ""
for i in range(N-1):
    if A[i] > A[i+1] and state == "":
        state = "minus"
    elif A[i] > A[i+1] and state == "plus":
        state = ""
        count += 1
    elif A[i] > A[i+1] and state == "minus":
        continue
    elif A[i] < A[i+1] and state == "":
        state = "plus"
    elif A[i] < A[i+1] and state == "minus":
        state = ""
        count += 1
    elif A[i] < A[i+1] and state == "plus":
        continue
    else:
        continue
print(count)



"""
今回のように短調増加や短調減少を確かめたい時，
n,*a=map(int,open(0).read().split())
ans=1
tmp=0
for i in range(1,n):
  if (a[i]-a[i-1])*tmp<0:
    ans+=1
    tmp=0
  elif not a[i]-a[i-1]==0:
    tmp=a[i]-a[i-1]
print(ans)
こうするのめっちゃいい
"""
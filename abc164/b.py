a,b,c,d = map(int, input().split(' '))

t,tmod = divmod(a, d)
a,amod = divmod(c , b)

if tmod >0:
  t = t+1
if amod >0:
  a = a+1

if a > t:
  print("No")
else:
  print("Yes")


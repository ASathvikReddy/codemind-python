from collections import deque
def monk_test(size,rota,a):
  if len(a)==size:
    de=deque(a)
    de.rotate(rota)
    a=list(de)
    return a

t=int(input())
while t>0:
  size,rota=map(int,input().split())
  a=list(map(int,input().split()))
  print(*monk_test(size,rota,a))
  t=t-1
  if t==0:
    break 
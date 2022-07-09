n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
m=999999
for i in range(n):
    if a[i]<x or a[i]>y:
        if m>a[i]:
            m=a[i]
if m==999999:
    print("-1")
else:
    print(m)
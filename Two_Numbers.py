n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(n):
    if a.count(a[i])==1:
        print(a[i],end=" ")
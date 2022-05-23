n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    temp=arr[i]
    d=0
    while temp:
        temp//=10
        d+=1
    if d%2==0:
        c+=1
print(c)

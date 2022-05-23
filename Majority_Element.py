n=int(input())
arr=list(map(int,input().split()))
m=-1
c=0
res=[]
for i in range(0,n):
    c=0
    for j in range(0,n):
        if arr[i]==arr[j]:
            c+=1
    if c>m:
        m=c
        res=arr[i]
    elif c==m:
        if arr[i]<res:
            res=arr[i]
print(res)
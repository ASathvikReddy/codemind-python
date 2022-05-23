n=int(input())
arr=list(map(int,input().split()))
c=0
d=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if arr[i]==arr[j] and i!=j:
            c+=1
    if c==0:
        print(arr[i],end=' ')
        d+=1
if d==0:
    print("-1")
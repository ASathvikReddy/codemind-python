n=int(input())
arr=list(map(int,input().split()))
c=0
ma=-1
for i in range(0,n):
    c=0
    for j in range(0,n):
        if arr[i]==arr[j]:
            c+=1
    if c==1:
        if arr[i]>ma:
            ma=arr[i]
if ma==0:
    print("-1")
else:
    print(ma)
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if arr[j]<arr[i]:
            c+=1
    print(c,end=' ')
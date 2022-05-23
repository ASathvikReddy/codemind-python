n=int(input())
a=list(map(int,input().split()))
arr=list()
for i in range(0,n):
    x=a[i]*a[i]
    arr.append(x)
for i in range(0,n):
    for j in range(0,n):
        if arr[i]<arr[j] and i!=j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(0,n):
    print(arr[i],end=' ')
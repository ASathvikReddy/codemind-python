arr=list(map(int,input().split()))
m1=m2=0
l=len(arr)
for i in range(0,l):
    if arr[i]>m1:
        if m1>m2:
            m2=m1
        m1=arr[i]
    elif arr[i]>m2 and arr[i]<=m1:
        m2=arr[i]
print((m1-1)*(m2-1))
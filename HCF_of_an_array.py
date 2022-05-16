n=int(input())
j=1
arr=list(map(int,input().split()))
hcf=arr[0]
for i in range(0,n):
    while j<n:
        if arr[j]%hcf==0:
            j+=1
        else:
            hcf=arr[j]%hcf
print(hcf)
n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in range(0,n):
    if i%2:
        os+=arr[i]
    elif i%2==0:
        es+=arr[i]
if (os-es)==0:
    print("YES")
else:
    print("NO")
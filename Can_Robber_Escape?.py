n=int(input())
arr=list(map(int,input().split()))
odd=0
for i in range(0,n):
    if arr[i]%2:
        odd+=1
if odd>2:
    print("NO")
else:
    print("YES")
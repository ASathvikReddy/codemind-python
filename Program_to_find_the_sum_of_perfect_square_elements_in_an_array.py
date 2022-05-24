n=int(input())
arr=list(map(int,input().split()))
pro=1
sum=0
for i in range(0,n):
    pro=1
    while pro*pro<=arr[i]:
        if pro*pro==arr[i]:
            sum+=arr[i]
        pro+=1
print(sum)
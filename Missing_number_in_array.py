n=int(input())
for i in range(0,n):
    m=int(input())
    arr=list(map(int,input().split()))
    for j in range(1,m+1):
        if j not in arr:
            print(j)
            break
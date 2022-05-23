n=int(input())
arr=list(map(int,input().split()))
m=int(input())
me=max(arr)
for i in range(0,n):
    if (arr[i]+m)>=me:
        print("True",end=' ')
    else:
        print("False",end=' ')
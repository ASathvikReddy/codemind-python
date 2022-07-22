def digit(n):
    if n==0:
        return 1
    if n<0:
        n*=-1
    c=0
    while n:
        r=n%10
        n//=10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    print(digit(a[i]),end=' ')
       

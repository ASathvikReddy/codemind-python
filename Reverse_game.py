def pali(n):
    rev=0
    temp=n
    while temp:
        rev=(rev*10)+(temp%10)
        temp//=10
    return rev
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    print(pali(a[i]),end=' ')
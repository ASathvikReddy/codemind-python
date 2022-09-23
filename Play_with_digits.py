def sepa(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s

n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=sepa(i)
print(s)
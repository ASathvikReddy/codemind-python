n=int(input())
pro=1
s=0
while n:
    r=n%10
    pro=pro*r
    s+=r
    n=n//10
res=pro-s
print(res)
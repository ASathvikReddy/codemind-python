def rev(n):
    r=0
    while n:
        r=r*10+n%10
        n//=10
    return r
n=int(input())
while True:
    n+=rev(n)
    if n==rev(n):
        break
print(n)
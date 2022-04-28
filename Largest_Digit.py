n=int(input())
a=0
max=0
while n:
    a=n%10
    n//=10
    if(a>max):
        max=a
print(max)
    
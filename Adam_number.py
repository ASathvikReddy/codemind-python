n=int(input())
sq=n*n
rev=0
while n:
    rev=(rev*10)+n%10
    n//=10
revsq=rev*rev
ans=0
while revsq:
    ans=(ans*10)+revsq%10
    revsq//=10
if ans==sq:
    print(True)
else:
    print(False)
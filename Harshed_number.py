n=int(input())
x=n
sum=0
while n:
    r=n%10
    sum+=r
    n//=10
if(x%sum==0):
    print("True")
else:
    print("False")
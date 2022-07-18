n=int(input())
sum=0
temp=n
while temp:
    r=temp%10
    temp//=10
    pro=1
    for i in range(1,r+1):
        pro*=i
    sum+=pro
if n==sum:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number") 


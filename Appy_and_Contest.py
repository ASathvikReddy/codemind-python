t=int(input())
for i in range(t):
    x,a,b,y=map(int,input().split())
    f=0
    if a%b==0:
        f=a
    elif b%a==0:
        f=b
    else:
        f=a*b
    g=x//f
    h=x//a
    i=x//b
    h=h-g
    i=i-g
    if i+h>=y:
        print("Win")
    else:
        print("Lose")
n=int(input())
while n:
    a=input()
    c=0
    b=list(a)
    for i in b:
        if ord(i)>=48 and ord(i)<=57:
            c=1
    if c==1:
        print("Yes")
    else:
        print("No")
    n-=1
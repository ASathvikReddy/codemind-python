n=int(input())
for i in range(n):
    a=int(input())
    rev=0
    temp=a
    while temp:
        rev=(rev*10)+(temp%10)
        temp//=10
    if(rev==a):
        print(True)
    else:
        print(False)
    
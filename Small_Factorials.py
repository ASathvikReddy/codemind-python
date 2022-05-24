n=int(input())
for i in range(0,n):
    x=int(input())
    fact=1
    for j in range(1,x+1):
        fact=fact*j
    print(fact)
n=int(input())
t=n-1
for i in range(1,n+1):
    for j in range(1,t+1):
        print(" ",end="")
    for k in range(1,2*i):
        print(i,end="")
    print()
    t-=1
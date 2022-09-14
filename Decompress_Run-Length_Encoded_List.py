n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n,2):
    b=a[i+1]
    for j in range(a[i]):
        l.append(b)
for i in l:
    print(i,end=" ")
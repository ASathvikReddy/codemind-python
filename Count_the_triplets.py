t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for k in range(len(a)):
        for j in range(len(a)):
            if a[k]!=a[j]:
                if a[k]+ a[j] in a:
                    c+=1
    if c==0:
        print("-1")
    else:
        print(c//2)
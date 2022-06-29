n=list(map(str,input().split()))
l=len(n)
for i in range(0,l):
    for j in range(0,l):
        if i!=j and len(n[i])<len(n[j]):
            t=n[i]
            n[i]=n[j]
            n[j]=t
print(*n)
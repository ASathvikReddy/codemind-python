n=int(input())
l=list(map(int,input().split()))
ans='NO'
for i in range(n):
        nob=0
        for j in range(n):
                if i&j:
                    nob+=l[j]
                else:
                    nob-=l[j]
        if nob%360==0:
            ans='YES'
print(ans)
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=max(a,b)
    ans=-1
    for i in range(c+1):
        if (i*i)%b==a:
            ans=i
            break
    print(ans)
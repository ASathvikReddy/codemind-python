t=int(input())
for i in range(t):
    s=input()
    l=[]
    for i in s:
        l.append(int(i))
    mi=min(l)
    ma=max(l)
    c=0
    a=[]
    for i in range(mi,ma+1):
        a.append(i)
    if sorted(l)==sorted(a):
        print("YES")
    else:
        print("NO")
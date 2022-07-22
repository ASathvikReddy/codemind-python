n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=d=0
a=set(a)
b=set(b)
for i in a:
    if i not in b:
        c+=1
for i in b:
    if i not in a:
        d+=1
print(c+d)
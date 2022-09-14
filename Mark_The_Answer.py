n,x=map(int,input().split())
a=list(map(int,input().split()))
f=0
c=0
for i in a:
    if i>x and f==1:
        break
    elif i>x:
        f+=1
    else:
        c+=1
print(c)
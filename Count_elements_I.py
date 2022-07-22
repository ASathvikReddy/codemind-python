n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a,b=set(a),set(b)
c=0
for i in a:
    if i in b:
        c+=1
print(c)
s=input()
c=input()
d=0
e=0
for i in s:
    if c in s:
        d=s.count(c)
        e=1
    else:
        e=0
if e==0:
    print("-1")
else:
    print(d)
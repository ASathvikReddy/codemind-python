n=int(input())
s=input()
c=0
d=0
for i in s:
    if i=="1":
        c+=1
    if i=="0":
        if c>d:
            d=c
        c=0
if d<c:
    d=c
print(d)
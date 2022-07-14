s=input()
c=d=0
i=0
while i<len(s):
    if s[i]=='z':
        c+=1
    else:
        d+=1
    i+=1
if 2*c==d:
    print("Yes")
else:
    print("No")
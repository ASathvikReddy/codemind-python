s=input()
c=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[j]==s[i]:
            c+=1
    if c==1:
        print(i)
        break
if c!=1:
    print("-1")
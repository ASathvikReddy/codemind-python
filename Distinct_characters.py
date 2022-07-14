s=input().replace(" ","").lower()
s1=''
for i in s:
    if s.count(i)==1:
        s1+=i
s2=sorted(s1)
for i in s2:
    if i!=" ":
        print(i,end='')
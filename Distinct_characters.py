n=input()
s=n.lower()
s=s.replace(" ","")
s1=[]
for i in range(len(s)):
    c=s.count(s[i])
    if c==1:
        s1.append(s[i])
s1.sort()
s1=str(s1)
s1=s1.replace(",","")
s1=s1.replace("[","")
s1=s1.replace("]","")
s1=s1.replace(",","")
s1=s1.replace("'","")
s1=s1.replace(" ","")
print(s1)
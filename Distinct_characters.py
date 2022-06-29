n=input()
n=n.lower()
n=n.replace(" ","")
s=set(n)
s=sorted(s)
for i in s:
    if i!=" ":
        print(i,end="")
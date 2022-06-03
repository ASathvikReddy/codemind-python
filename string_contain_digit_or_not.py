a=input()
c=0
count=0
b=list(a)
for i in b:
    if ord(i)>=48 and ord(i)<=57:
        count+=1
        c=1
if c==1:
    print("Contains",count,"digit")
else:
    print("Doesn't contain digit")

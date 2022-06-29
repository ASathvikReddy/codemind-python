a=input()
b=input()
a=a.split(" ")
b=b.split(" ")
c=0
for i in a:
    s=0
    x=0
    if i in b:
       s=a.count(i)
       x=b.count(i)
       if s==1 and x==1:
           c+=1
print(c)

n=input().lower()
x=y=0
for i in n:
    if i=='u':
        y+=1
    elif i=='d':
        y-=1
    elif i=='r':
        x+=1
    elif i=='l':
        x-=1
if x==0 and y==0:
    print(True)
else:
    print(False)
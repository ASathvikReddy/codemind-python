t=int(input())
c=0

while t:
    s=input()
    if s[1]=="+":
        c+=1
    else:
        c-=1
    t-=1
print(c)
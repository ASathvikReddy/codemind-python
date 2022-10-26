t=int(input())
for i in range(t):
    n=int(input())
    s=bin(n)
    c=0
    for i in s:
        if i=='1':
            c+=1
    print(c)
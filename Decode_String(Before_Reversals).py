t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    s=input()
    while b>0:
        li=s[:b]
        s=li[::-1]+s[b:]
        b-=1
    print(s)
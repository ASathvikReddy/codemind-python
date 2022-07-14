s=input()
n=int(input())
m=int(input())
for i in range(len(s)):
    if i>=n and i<=m:
        print(s[i],end='')
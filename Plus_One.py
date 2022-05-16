n=int(input())
t=0
arr=list(map(int,input().split()))
for i in range(n):
    t=t*10+arr[i]
t+=1
s=str(t)
for i in s:
    print(i,end=' ')
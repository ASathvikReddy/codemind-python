n=int(input())
arr=list(map(int,input().split()))
m=int(input())
bee=list(map(int,input().split()))
o=int(input())
c=0
for i in range(0,n):
    if arr[i]<=o and bee[i]>=o:
        c+=1
print(c)
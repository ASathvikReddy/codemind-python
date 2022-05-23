n=int(input())
arr=list(map(int,input().split()))
res=0
c=0
new=list()
for i in arr:
    if i not in new:
        c=0
        new.append(i)
        for j in range(0,n):
            if i==arr[j]:
                c+=1
        res+=c//2
print(res)
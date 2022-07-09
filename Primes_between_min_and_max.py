def prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
a=list(map(int,input().split()))
c=0
mi,ma=a[0],a[0]
mini,maxi=0,0
for i in range(n):
    if a[i]<mi:
       mi=a[i]
       mini=i
    if  a[i]>ma:
        ma=a[i]
        maxi=i
if mini<maxi:
    for i in range(mini,maxi+1):
        if prime(a[i]):
            c+=1
else:
    for i in range(maxi,mini+1):
        if prime(a[i]):
            c+=1
print(c)
arr=list(map(int,input().split()))
bee=list(map(int,input().split()))
x=y=0
for i in range(0,3):
    if arr[i]>bee[i]:
        x+=1
    elif arr[i]<bee[i]:
        y+=1
print(x,y)
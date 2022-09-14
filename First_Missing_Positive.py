n=int(input())
a=list(map(int,input().split()))
i=1
while 1:
    if i not in a:
        print(i)
        break
    i+=1

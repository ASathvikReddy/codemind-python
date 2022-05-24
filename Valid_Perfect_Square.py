def perfect(n):
    a=1
    while a<n:
        sq=a*a
        if(sq==n):
            return 1
        a+=1
    return 0
        
n=int(input())
for i in range(0,n):
    a=int(input())
    if(perfect(a)):
        print("True")
    else:
        print("False")
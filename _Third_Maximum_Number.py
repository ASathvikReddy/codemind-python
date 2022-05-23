n=int(input())
arr=list(map(int,input().split()))
m=sorted(list(set(arr)))
print(m[len(m)-3])
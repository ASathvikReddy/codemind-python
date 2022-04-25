a,b,c = map(int,input().split())
s=float((a+b+c)/2)
area=float((s*(s-a)*(s-b)*(s-c))**0.5)
print('%.2f'%area)
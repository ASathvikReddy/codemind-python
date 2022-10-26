def set_bit(n,m):
    return ((1<<m)|n)
    
n,m=map(int,input().split())
print(set_bit(n,m))
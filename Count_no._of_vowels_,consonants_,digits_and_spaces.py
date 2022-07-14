s=input().lower()
v=c=d=p=0
for i in s:
    if i in "aeiou":
        v+=1
    if i in "bcdfghjklmnpqrstvwxyz":
        c+=1
    if i in "1234567890":
        d+=1
    if i==' ':
        p+=1
print('Vowels:',v)
print('Consonants:',c)
print('Digits:',d)
print('White spaces:',p)
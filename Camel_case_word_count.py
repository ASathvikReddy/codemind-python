def wordcount(s): 
    count = 1
    for i in range(1, len(s)-1): 
            if (s[i].isupper()):
                count+=1 
    return count
s=input()
print(wordcount(s))
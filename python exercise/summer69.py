
def summer_69(a):
    lis=a.copy()
   
    sum=0
    first=0
    last=0
    for i in a:
        if i ==6:
            first = a.index(i)
            for j in a:
                if j==9:
                    last= a.index(j)
            
    for j in range(0,first):   
        sum+=lis[j]
    if last==0:
        last=last-1
    for i in range(last+1,len(lis)):
        sum+=lis[i]
    return sum
    


print(summer_69([2, 1, 6, 9, 11]))
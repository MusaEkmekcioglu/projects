a=input("enter a word=")
count=0
for i in a:
    count+=1
    if count<len(a):
        i=i +"-"
    print(i, end="")
        

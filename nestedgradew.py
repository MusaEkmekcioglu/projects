student=[]
mylistscore=[]
mylistname=[]
a=[]
b=[]
c=[]
low=100
for i in range(int(input("number"))):

    name=str(input("name="))
    score=float(input("score="))
    
    if low>score:
        low=score
    student.append([name,score])

for i in student:
    mylistscore.append(i[1])
    mylistname.append(i[0])
    a=sorted(mylistscore)

for i in student:
    if a[0] in i:
        b.append(i[0])
    elif a[1] in i:
        b.append(i[0])

c=sorted(b)

print(student)
print("en dusuk alanlarin notlar = "+ str(a[0])+" " + str(a[1]))   
print("isimleri= "+ str(b))     
        
            
            


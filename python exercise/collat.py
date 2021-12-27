#ni çift sayıysa: ni+1=ni/2
#ni tek sayıysa: ni+1=3ni+1

a=int(input("enter a number= "))
mylist=[]
mylist.append(a)
    
count=a
while count>1:
    if count%2==0:
        count= int(count/2)
        mylist.append(count)
        if count==2:
            break
    if count%2!=0:
        count=3*count+1
        mylist.append(count)
mylist.append(1)
print(mylist)
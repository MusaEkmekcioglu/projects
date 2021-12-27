mylist=[]
mylist2=[]
a=int(input("enter a number="))
for i in range(a):
    mylist.append(i)

for j in range(2,a):
    for i in range(2,j):
        if j%i==0:
          break
    else:
        mylist2.append(j)
print(mylist2)
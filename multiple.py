a=int(input("enter a number="))

for i in range(0,11):
    print(str(a)+"x"+str(i)+"=",str(a*i))

for i in range(11):
    print("{} x{} =".format(a,i),a*i)

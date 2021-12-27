
sentence=list(input("enter a sentence, please = ").lower().split(" "))
list_my=list(range(1,29))
a=0
b=0
abc=dict()
for i in range(ord('a'), ord('z')+1):
  abc.update({chr(i):list_my[a]})
  a+=1
#print(abc)
a=0
c=""
for i in sentence:
    for j in range(len(i)):
        a=a+abc.get(list(i)[j])
        #print(i +" kelimenin puani " + str(a))
    if  a>b:
        b=a
        c=i
        a=0 
    else:
        a=0
print("en yuksek puan " + c +" puani= "+ str(b))

    
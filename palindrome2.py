#tek kelime icin 
"""
word = input("bir kelime girin=")
b=word.split()
c=list(word)
k=0
flag=False
for i in b:
    for j in i:
                
        if j==c[len(word)-1-k]:
            flag=True
        else:
            flag=False
        k+=1
print(flag)

"""
word = input("bir kelime girin=")
a="".join(reversed(word))
if word==a:
    print("yes")

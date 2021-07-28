anagram=input("enter a word =")
anagram_list=[] 
result=[]
b=0
while True:
    a=input("enter a word list =  Q use to for Quit    ").lower()
    if a =="q":
        break
    else:
        anagram_list.append(a)

    
for i in anagram_list:
    if sorted(list(i)) == sorted(anagram):
        result.append(i)
print(result)
  
             

def cchar(cc):
    liste=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    liste1=["A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    return liste1[-(liste.index(cc)+1)]

a=str(input("eneter a word = "))
word2=""
for i in a:
    if i ==" ":
        word2+=" "
        continue
    else:
        word2+=cchar(i)
print(word2.lower())
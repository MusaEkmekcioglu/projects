Right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]

Left = ["q","w" ,"e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]

word=set(input("enter a word="))
print(word)

if word.intersection(set(Right))==word:
    print(False)
elif word.intersection(set(Left))==word:
    print(False)
else:
    print(True)
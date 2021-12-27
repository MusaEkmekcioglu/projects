sentence=input("enter a sentence=").split()
i=0
longest=0
while i<len(sentence):
    if len(sentence[i])>longest:
        longest=len(sentence[i])
        b=sentence[i]
    i+=1
print(str(longest) + "   " + b)
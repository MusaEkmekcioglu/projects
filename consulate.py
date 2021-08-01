number=[11,36,33,66,89,21,32,16,10]
odd=[]
edd =[]
for i in number:
    [odd.append(i)  if i % 2 else edd.append(i) ]
print(odd)
print(edd)


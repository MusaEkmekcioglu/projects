"""
a=int(input("tekrar sayisini girin ="))
flag=True
c=0
b=[]
d=0
while flag:
    c+=1
    b.append(int(input("sayi girin= ")))
    if c==a:
        break
print(b)
for i in b:
    if i>d:
        d=i
print(d)
"""


strs = ["eat","tea","tan","ate","nat","bat"]
str=''
result={}

for i in strs:
    str="".join(sorted(i))
    
    if str in result:
        result[str].append(i)
    else:
        result[str]=[i]
        result[str].append(i)
print(result.items())
    
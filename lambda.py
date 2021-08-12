print((lambda x: x[::-1])([1,2,3,4,5]))
for x in [1,2,3,4,5]:
    print(x,(lambda x: 'odd'  if x %2 !=0 else 'even')(x))
nums1=[2,3,4,5]
nums2=[3,4,5,6]
a=map(lambda x,y: x+y,nums1,nums2)
print(list(a))

kelimeler=["alinin duasi","keremin babasi ","musanin arkadaslari "]

b=map(len,kelimeler)
c=map(lambda x: len(x) ,kelimeler)
print(list(b))
print(list(c))
kelimeler2=["alinin ","kere","musanslari "]
d=filter(lambda x:len(x)<5, kelimeler2 )
print(list(d))


first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sesliharf=["a","e",'i','o','u']

sesli=filter(lambda x: True if x in sesliharf else False , first_ten )
print(list(sesli))
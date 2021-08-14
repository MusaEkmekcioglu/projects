fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}

fruits_name=[x for x in fruits.keys()]
print(fruits_name)


i = 5
while True:
    if i%0xe == 0:
        break
    print(i)
    i += 1

x = 'abcd'
for i in range(len(x)):
    x[i].upper()
print (x)

k=[2,3,4]
print(list(reversed(k)))

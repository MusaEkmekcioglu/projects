number = input('Enter a number  ')
total = 0
sayac = 1
for i in number:
    print(i)
    total = (int(i) ** sayac) + total
    sayac += 1
print(total)
if total == int(number):
    print('{} is a Disarium number.'.format(number))
else:
    print('{} is not a Disarium number.'.format(number))
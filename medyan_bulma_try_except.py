liste = []
while True:
    try:
        giris = input("Enter a number or 'q' to quit > ")
        int(giris)
        liste.append(int(giris))
    except:
        print('Cikis yaptiniz ya da yanlis bir tusa bastiniz.')
        break
liste.sort()
print(liste)
deger = len(liste)
if deger % 2 == 0:
    nott = deger // 2
    medyan = (liste[nott - 1] + liste[nott]) // 2
else:
    nott = (deger + 1) // 2
    medyan = liste[nott - 1]
print(f'Medyan: {medyan}')
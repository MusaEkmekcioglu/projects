dictt = {1 : 'Domates', 2 : 'Sogan', 3 : 'Biber', 4 : 'Yumurta', 5 : 'Elma', 6 : 'Armut'}
liste = []
print(" Hosgeldiniz!\
Domates icin 1'i, Sogan icin 2'yi, Biber icin 3'u, \
Yumurta icin 4'u, Elma icin 5'i, Armut icin 6'yi seciniz. Cikmak icin Q ya basiniz")

while True:
    result= input("Secmek istediginiz urunun numarasini giriniz ya da cikmak icin 'q' tusuna basiniz.").lower()
    
    if result=="q":
        print("cikis yapiliyor")
        break
    elif dictt[int(result)]==1 or 2 or 3 or 4 or 5 or 6:
            liste.append(dictt[int(result)])
            
    else:
        print("dukkanda yok, yanlis secim gule gule ")
        break
print(liste)
for i in range(5):

    print("urun = {}  sayisi = {}" .format( liste[i] , liste.count(dictt[i+1])) )




#sayı okunuşları
from functools import reduce
rakamlar = {1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
onluklar = {10:"On",20:"Yirmi",30:"Otuz",40:"Kırk",50:"Elli",60:"Altmış",70:"Yetmiş",80:"Seksen",90:"Doksan"}
yüzlükler = {100:"Yüz"}

# 327 = 3 * 100 + 2 * 10 + 7
def okunus(girdi):

    girdi = int(girdi)
    girdiler = []

    yüzlük = (girdi // 100)
    onluk = ((girdi % 100) // 10 ) *10
    birlik = (girdi % 100) % 10

    girdiler.append(yüzlük)
    girdiler.append(100)
    girdiler.append(onluk)
    girdiler.append(birlik)

    okunus = []

    for i in girdiler:
        if i in rakamlar.keys():
            okunus.append(rakamlar[i])
        elif i in onluklar.keys():
            okunus.append(onluklar[i])
        elif i in yüzlükler.keys():
            okunus.append(yüzlükler[i])

    return reduce(lambda x,y: x + " " + y , okunus)


girdi = input("girdi giriniz: ")
print(okunus(girdi))
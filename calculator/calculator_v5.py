import math
from functools import reduce
from time import sleep
from colorama import Fore , init
init(autoreset=True)

#   12+21-14*47/91

numbers = ("0","1","2","3","4","5","6","7","8","9")
operator = ("*","/","+","-")
parantez = ("(",")")

carpma = lambda x,y: x*y
bolme = lambda x,y: x/y
toplama = lambda x,y : x + y
cikartma = lambda x,y : x - y

carpilacak = list()
bolunecek = list()
toplanacak = list()
cikartilacak = list()


def girdi_al():
    girdi = input("İşlemi Giriniz:")

    girdiler = list()
    sayi = ""

    for i in girdi:
        if i in numbers:  # NUMARALAR GELDİĞİNDE ÇALIŞACAK

            sayi += i

        elif (i in operator) :  # OPERATÖRLER GELDİĞİNDE ÇALIŞACAK

            try:
                girdiler.append(int(sayi))
                sayi = ""
            except ValueError:
                pass
            girdiler.append(i)

        elif i in parantez:  # PARANTEZLER GELİNCE ÇALIŞACAK

            if i == parantez[0]:
                girdiler.append(i)
                try:
                    girdiler.append(int(sayi))
                    sayi = ""
                except ValueError:
                    pass

            else:
                try:
                    girdiler.append(int(sayi))
                    sayi = ""
                except ValueError:
                    pass
                girdiler.append(i)

        elif i == " ":
            pass

        else:
            print(Fore.RED + "Geçersiz Karakter Kullanımı.")

    try:
        girdiler.append(int(sayi))
    except ValueError:
        pass

    print(girdiler)
    return girdiler


def ayikla(dongu):

    for i in dongu:
        indx = dongu.index(i)

        if i == operator[0]:
            carpilacak.append(dongu[indx-1])
            carpilacak.append(dongu[indx+1])
            dongu.pop(indx + 1)
            dongu.pop(indx)
            dongu.pop(indx - 1)
        elif i == operator[1]:
            bolunecek.append(dongu[indx-1])
            bolunecek.append(dongu[indx+1])
            dongu.pop(indx + 1)
            dongu.pop(indx)
            dongu.pop(indx - 1)
        elif i == operator[2]:
            toplanacak.append(dongu[indx-1])
            toplanacak.append(dongu[indx+1])
            dongu.pop(indx + 1)
            dongu.pop(indx)
            dongu.pop(indx - 1)
        elif i == operator[3]:
            cikartilacak.append(dongu[indx-1])
            cikartilacak.append(dongu[indx+1])
            dongu.pop(indx + 1)
            dongu.pop(indx)
            dongu.pop(indx - 1)


    return carpilacak,bolunecek,toplanacak,cikartilacak

#def hesapla():





def parantezle():
    girdiler = girdi_al()

    indx0 = girdiler.index(parantez[0])
    indx1 = girdiler.index(parantez[1])

    parantez_ici = girdiler[indx0+1:indx1]
    print(parantez_ici)

    print(ayikla(parantez_ici))

    #return girdiler


parantezle()























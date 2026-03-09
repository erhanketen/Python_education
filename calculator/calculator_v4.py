#import math                                              // Bu kısım henüz yok
from colorama import Fore , init
init(autoreset=True)
from time import sleep

operators = ( "*" , "/" , "+" , "-" )
numbers = ("0","1","2","3","4","5","6","7","8","9",".")
#fonksiyonlar = ("sqrt" , "cos" , "sin" , "sq" , "log" )   // Bu kısım henüz yok

girdiler_son = []

def girdi_al():
    total_sayı = ""
    sayı = []
    girdiler = []
    while True:
        girdi = input("İşlemleri Girin:")

        if girdi in numbers:
            sayı.append(girdi)

        elif girdi in operators:
            for i in sayı:
                total_sayı += i

            girdiler.append(total_sayı)
            total_sayı = ""
            sayı = []
            girdiler.append(girdi)

        else:
            if girdi == "=":
                for i in sayı:
                    total_sayı += i
                girdiler.append(total_sayı)
                break
            else:
                print(Fore.RED + "Geçersiz Operatör veya Rakam Girdiniz!")

    for i in girdiler:
        try:
            i = int(i)
            girdiler_son.append(i)
        except ValueError:
            try:
                i = float(i)
                girdiler_son.append(i)
            except ValueError:
                girdiler_son.append(i)


def calculate():
    girdi_al()
    for i in girdiler_son:
        indx = girdiler_son.index(i)
        if i == operators[0]:
            girdiler_son[indx+1] = girdiler_son[indx-1] * girdiler_son[indx+1]
            girdiler_son.pop(indx)
        elif i == operators[1]:
            girdiler_son[indx + 1] = girdiler_son[indx - 1] / girdiler_son[indx + 1]
            girdiler_son.pop(indx)
        elif i == operators[2]:
            girdiler_son[indx + 1] = girdiler_son[indx - 1] + girdiler_son[indx + 1]
            girdiler_son.pop(indx)
        elif i == operators[3]:
            girdiler_son[indx + 1] = girdiler_son[indx - 1] - girdiler_son[indx + 1]
            girdiler_son.pop(indx)
    if girdiler_son == [""]:
        print(Fore.RED + "Hiç Bir İşlem Girmediniz")
        return "error"
    else:
        return girdiler_son[-1]


print(Fore.LIGHTBLUE_EX +"""
---------------------------------------------


               - CALCULATOR -


---------------------------------------------
""")

sonuc = calculate()
if sonuc == "error":
    pass
else:
    print(Fore.LIGHTWHITE_EX+"Hesaplanıyor...")
    sleep(1.5)
    print(Fore.GREEN + "İşlemin Sonucu = {}".format(sonuc))
while True:
    feedback  = input("Başka İşlem Yapacak mısınız? (y/n):")
    if feedback == "y" or feedback == "Y":
        girdiler_son = []
        sonuc = calculate()
        sleep(1.5)
        print(Fore.LIGHTWHITE_EX+"Hesaplanıyor...")

    elif feedback == "n" or feedback == "N":
        print(Fore.LIGHTWHITE_EX + "Kapatılıyor...")
        sleep(0.7)
        break

    else:
        print(Fore.RED + "Geçersiz tuşlama yaptınız!\nSadece y veya n cevabı lütfen...")



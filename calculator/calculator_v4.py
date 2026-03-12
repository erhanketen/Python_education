import math
from colorama import Fore , init
init(autoreset=True)
from time import sleep

operators = ( "*" , "/" , "+" , "-" )
numbers = ("0","1","2","3","4","5","6","7","8","9",".")
fonksiyonlar = ("sqrt" , "cos" , "sin" , "sq" , "log" )

girdiler_son = []

def girdi_al():
    total_sayı = ""
    sayı = []
    girdiler = []
    while True:
        girdi = input("İşlemleri Girin:")

        if girdi in numbers:
            sayı.append(girdi)

        elif girdi in fonksiyonlar:
            girdiler.append(girdi)

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
    a = 0
    while a < len(girdiler_son):
        for i in girdiler_son:
            try:
                indx = girdiler_son.index(i)
                if i == "sqrt":
                    if girdiler_son[indx+1] in fonksiyonlar:
                        pass
                    elif not girdiler_son[indx+1] in (numbers or fonksiyonlar):
                        raise SyntaxError
                    else:
                        girdiler_son[indx] = math.sqrt(girdiler_son[indx+1])
                        girdiler_son.pop(indx+1)
                elif i == "cos":
                    if girdiler_son[indx+1] in fonksiyonlar:
                        pass
                    elif not girdiler_son[indx+1] in (numbers or fonksiyonlar):
                        raise SyntaxError
                    else:
                        girdiler_son[indx] = math.cos(girdiler_son[indx+1])
                        girdiler_son.pop(indx+1)
                elif i == "sin":
                    if girdiler_son[indx+1] in fonksiyonlar:
                        pass
                    elif not girdiler_son[indx+1] in (numbers or fonksiyonlar):
                        raise SyntaxError
                    else:
                        girdiler_son[indx] = math.sin(girdiler_son[indx+1])
                        girdiler_son.pop(indx+1)
                elif i == "sq":
                    if girdiler_son[indx+1] in fonksiyonlar:
                        pass
                    elif not ((girdiler_son[indx+1] == int) or (girdiler_son[indx+1] in fonksiyonlar)):
                        raise SyntaxError
                    else:
                        girdiler_son[indx] = math.pow(girdiler_son[indx+1],2)
                        girdiler_son.pop(indx+1)
                elif i == "log":
                    if girdiler_son[indx+1] in fonksiyonlar:
                        pass
                    elif not girdiler_son[indx+1] in (numbers or fonksiyonlar):
                        raise SyntaxError
                    else:
                        girdiler_son[indx] = math.log10(girdiler_son[indx+1])
                        girdiler_son.pop(indx+1)
            except TypeError:
                print(Fore.RED + "Fonksiyondan Sonra Operatör Kullanılamaz!")
                return "error"
            except SyntaxError:
                print(Fore.RED + "Fonksiyonlar Arasında Operatör Kullanmalı veya Fonksiyona Değer Vermelisiniz!")
                return "error"
            a += 1


    for i in girdiler_son:
        try:
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
        except TypeError:
            print(Fore.RED +"Üst Üste Operatör Kullanılamaz!")
            return "error"

    if girdiler_son == [""]:
        print(Fore.RED + "Hiç Bir İşlem Girmediniz")
        return "error"
    else:
        return girdiler_son[-1]


print(Fore.LIGHTBLUE_EX +"""
---------------------------------------------


               - CALCULATOR -


---------------------------------------------
"""
      """
FONKSİYONLAR:
1- sqrt: Karekök alır     
2- cos: Kosinüs alır
3- sin: Sinüs alır
4- sq: Kare alır
5- log: 10 tabanında logaritma alır      
      """)

sonuc = calculate()
if sonuc == "error":
    sleep(2)
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
        if sonuc == "error":
            sleep(2)
            continue
        print(Fore.LIGHTWHITE_EX+"Hesaplanıyor...")
        sleep(1.5)
        print(Fore.GREEN + "İşlemin Sonucu = {}".format(sonuc))
    elif feedback == "n" or feedback == "N":
        print(Fore.LIGHTWHITE_EX + "Kapatılıyor...")
        sleep(0.7)
        break

    else:
        print(Fore.RED + "Geçersiz tuşlama yaptınız!\nSadece y veya n cevabı lütfen...")



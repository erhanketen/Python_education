from math import log , pow , sqrt , factorial , cos , sin, tan, atan, acos, asin  , radians , degrees
from time import sleep
from colorama import Fore , init
init(autoreset=True)

# (12-6)*4+5/10

fonksiyonlar = ("log","pow","sqrt","factorial","cos","sin","tan","atan","acos","asin","ANS")


def girdi_al(girdi):   # Bu fonksiyon girdi alır, listeler ve integer'a çevirir.
    numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")
    operators = ("*", "/", "+", "-","(",")",","," ")

    girdiler = list()
    num = ""
    func = ""


    for i in girdi:
        if func in fonksiyonlar:
            if func == "ANS":
                try:
                    girdiler.append(ANS)
                except NameError:
                    return "IndexError"
            else:
                girdiler.append(func)
            func = ""
        if i in numbers:
            num += i
        elif i in operators:
            if num == "":
                girdiler.append(i)
            elif i == " ":
                pass
            else:
                try:
                    girdiler.append(float(num))
                    num = ""
                except ValueError:
                    return "SyntaxError"
                finally:
                    if i != ",":
                        girdiler.append(i)

        elif i not in numbers or i not in operators:
            func += i



    if num != "":
        try:
            girdiler.append(float(num))
        except ValueError:
            return "SyntaxError"


    for i in girdiler:
        if (i not in fonksiyonlar) and (i not in operators) and (type(i) != int and type(i) != float):
            return "SyntaxError"

    if func:
        return "SyntaxError"

    if not girdiler:
        return "NoProcessError"

    return girdiler

def tokenleme(girdiler):   #Bu Fonksiyon işlemi Postfix'e dönüştürür. (Shunting Yard Algoritması)

    oncelik = { "*":2 , "/": 2 , "+": 1 , "-" : 1 }
    yigin = []
    cıktı = []

    for i in girdiler:

        if type(i) == int or type(i) == float:
            cıktı.append(i)

        elif i in oncelik:

            while (yigin and yigin[-1] in oncelik and oncelik[yigin[-1]] >= oncelik[i]) or (yigin and yigin[-1] in fonksiyonlar):
                cıktı.append(yigin.pop())
            yigin.append(i)

        elif i in fonksiyonlar:
            yigin.append(i)

        elif i == "(":
            yigin.append(i)

        elif i == ")":
            if "(" not in yigin:
                return "SyntaxError"

            while (yigin[-1] != "("):
                cıktı.append(yigin.pop())
            yigin.pop()

    while yigin:
        cıktı.append(yigin.pop())

    return cıktı

# [12, 6, '-', 4, '*', 5, 10, '/', '+']

def calculate(cikti):

    yigin = []

    operators = ("*","/","+","-")

    for i in cikti:
        if type(i) == int or type(i) == float:
            yigin.append(i)

        elif i in operators:
            try:

                b = yigin.pop()
                a = yigin.pop()

                if i == operators[0]:
                    yigin.append(a * b)
                elif i == operators[1]:
                    yigin.append(a / b)
                elif i == operators[2]:
                    yigin.append(a + b)
                elif i == operators[3]:
                    yigin.append(a - b)
            except IndexError:
                return "OperatorError"
        elif i in fonksiyonlar:
            try:
                if not yigin:
                    return "SyntaxError"
                if i == fonksiyonlar[0]:
                    b = yigin.pop()
                    a = yigin.pop()
                    yigin.append(log(a,b))
                elif i == fonksiyonlar[1]:
                    b = yigin.pop()
                    a = yigin.pop()
                    yigin.append(pow(a,b))
                elif i == fonksiyonlar[2]:
                    a = yigin.pop()
                    yigin.append(sqrt(a))
                elif i == fonksiyonlar[3]:
                    a = yigin.pop()
                    try:
                        a = int(a)
                    except ValueError:
                        return "ValueError"
                    yigin.append(factorial(a))
                elif i == fonksiyonlar[4]:
                    a = yigin.pop()
                    if a == 90 or 270:
                        yigin.append(0)
                    else:
                        a = radians(a)
                        yigin.append(cos(a))
                elif i == fonksiyonlar[5]:
                    a = yigin.pop()
                    a = radians(a)
                    yigin.append(sin(a))
                elif i == fonksiyonlar[6]:
                    a = yigin.pop()
                    a = radians(a)
                    yigin.append(tan(a))
                elif i == fonksiyonlar[7]:
                    a = yigin.pop()
                    yigin.append(degrees(atan(a)))
                elif i == fonksiyonlar[8]:
                    a = yigin.pop()
                    yigin.append(degrees(acos(a)))
                elif i == fonksiyonlar[9]:
                    a = yigin.pop()
                    yigin.append(degrees(asin(a)))
            except IndexError:
                return "IndexError"
    if len(yigin) != 1:
        return "SyntaxError"
    else:
        return yigin[0]

print(Fore.LIGHTRED_EX+"""
----------------------------------------------


                 -CALCULATOR-
        
        
----------------------------------------------

FONKSİYONLAR:
1-) log
2-) pow
3-) sqrt 
4-) factorial
5-) cos
6-) sin
7-) tan
8-) atan
9-) acos
10-) asin

# ANS --> en son sonuç
""")


while True:
    girdi = input(Fore.LIGHTWHITE_EX+"İşlemleri Giriniz (çıkış 'exit'):")
    if girdi == "exit":
        print(Fore.LIGHTWHITE_EX+"Kapatılıyor...")
        sleep(1)
        break
    girdiler = girdi_al(girdi)
    if girdiler == "NoProcessError":
        print(Fore.RED+"Bir İşlem Girmediniz!")
        continue
    elif girdiler == "SyntaxError":
        print(Fore.RED+"Geçersiz Bir Girdi Girdiniz!")
        continue
    elif girdiler == "IndexError":
        print(Fore.RED+"ANS Mevcut Değil!")
        continue
    cikti = tokenleme(girdiler)
    if cikti == "SyntaxError":
        print(Fore.RED+"Geçersiz Bir Girdi Girdiniz!")
        continue
    elif cikti == "ValueError":
        print(Fore.RED+"Fonksiyona Geçersiz Bir Değer Verdiniz!")
        continue
    elif cikti == "IndexError":
        print(Fore.RED+"Fonksiyon Kullanımı Geçersiz!")
        continue
    elif cikti == "OperatorError":
        print(Fore.RED+"Yanlış Operatör Kullanımı!")
        continue
    sonuc = calculate(cikti)
    if sonuc == "SyntaxError":
        print(Fore.RED+"Geçersiz Bir Girdi Girdiniz!")
        continue
    elif sonuc == "ValueError":
        print(Fore.RED + "Bu Fonksiyona Sadece Tam Sayi Değerler Verilebilir!")
        continue
    elif sonuc == "IndexError":
        print(Fore.RED + ("Geçersiz Fonksiyon Kullanımı!"))
        continue
    elif sonuc == "OperatorError":
        print(Fore.RED+"Geçersiz Operatör Kullanımı!")
        continue
    ANS = sonuc
    print(Fore.LIGHTWHITE_EX+"Hesaplanıyor...")
    sleep(1)
    print(Fore.GREEN+"{} = {}".format(girdi, sonuc))


"""
-----------------------------------------------------------------------------
ÖNEMLİ PROBLEMLER:
1- Negatif değerli sayılar kullanılırsa hata döner.  :C
2- İç içe fonksiyonlarda yanlış değer döner.  :C
-----------------------------------------------------------------------------
DEĞERLİ GELİŞMELER:
1- Algoritma Daha Basit ve Güvenilir Çalışıyor.  :D
2- Fonksiyonlar Daha Efektif Kullanılabiliyor.  :D
3- İşlem Önceliği ve Parantez Kavramı Mevcut.  :D
4- Hata Yakalamalar ve Döngüler Sayesinde Program Kesilmeden Çalışabiliyor.  :D
-----------------------------------------------------------------------------
"""



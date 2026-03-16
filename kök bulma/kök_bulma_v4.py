from time import sleep
from colorama import Fore , init
init(autoreset=True)

def girdi_al(girdi):

    numbers = ("0","1","2","3","4","5","6","7","8","9")
    operators = ("+","-","x","^")


    girdiler = list()
    num = ""

    for i in girdi:

        if i in numbers:
            num += i

        elif i in operators:
            if num != "":
                try:
                    girdiler.append(int(num))
                    num = ""
                    girdiler.append(i)

                except ValueError:
                    return "NotIntegerError"
            else:
                girdiler.append(i)
        elif i == " ":
            pass
        else:
            return "SyntaxError"

    if num != "":
        try:
            girdiler.append(int(num))
        except ValueError:
            return "NotIntegerError"

    return girdiler


def indexle(girdiler):

    operator = ("x","^")
    sembol = ("+","-")

    yigin= []
    cikti = []
    op = ""

    for i in girdiler:

        if i in sembol:
            if op == "x":
                yigin.append(op)
                op = ""
            yigin.append(i)

        elif i in operator:
            op += i

        elif type(i) == int:
            if op == "x^":
                i = str(i)
                op += i
                yigin.append(op)
                op = ""
            else:
                cikti.append(i)
    if op != "":
        yigin.append(op)



    denklem = []
    try:
        while yigin:
            i = yigin.pop()
            if i == "-":
                if cikti:
                    sayi = cikti.pop() * -1
                    denklem.append(sayi)
                else:
                    denklem.append(-1)
            elif i == "+" and cikti:
                denklem.append(cikti.pop())
            elif i == "x":
                denklem.append(i)
            elif i == "x^2":
                denklem.append(i)

        while cikti:
            denklem.append(cikti.pop())
    except IndexError:
        return "IndexError"

    if denklem.count("x") == 2:
        return "IndexError"

    return denklem[::-1]


def kok_bul(denklem):

    yigin = []

    for i in denklem:
        if type(i) == int:
            yigin.append(i)
        elif i == "x^2":
            if yigin:
                a = yigin.pop()
            else:
                a = 1
        elif i == "x":
            b = yigin.pop()

    if yigin:
        c = yigin.pop()
    else:
        c = 0

    try:
        a
    except UnboundLocalError:
        return "NotSquareError"

    try:
        b
    except UnboundLocalError:
        b = 0

    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "NoRealRoot"
    kok1 = (-b+(delta**0.5))/(2*a)
    kok2 = (-b-(delta**0.5))/(2*a)

    return [kok1,kok2]

print(Fore.LIGHTRED_EX+"""
----------------------------------------------------


   İKİNCİ DERECEDEN BİR DENKLEMİN KÖKLERİNİ BULMA


----------------------------------------------------
""")
while True:
    girdi = input(Fore.LIGHTWHITE_EX+"Denklemi Giriniz (çıkmak için 'exit'):")
    if girdi == "exit":
        print(Fore.LIGHTWHITE_EX+"Kapatılıyor...")
        sleep(1)
        break
    girdiler = girdi_al(girdi)
    if girdiler == "NotIntegerError":
        print(Fore.RED+"Sadece Tam Sayı Girmelisiniz!")
        continue
    elif girdiler == "SyntaxError":
        print(Fore.RED+"Geçersiz Karakter Kullanımı!")
        continue
    denklem = indexle(girdiler)
    if denklem == "IndexError":
        print(Fore.RED+"Geçersiz Bir Girdi Girdiniz!")
        continue
    kokler = kok_bul(denklem)
    if kokler == "NotSquareError":
        print(Fore.RED+"Denklemde x^2 İfadesi Yok!")
        continue
    print(Fore.LIGHTWHITE_EX+"Hesaplanıyor...")
    sleep(1)
    if kokler[0] == kokler[1]:
        print(Fore.LIGHTGREEN_EX+"Çift Katlı Kök: {}".format(kokler[0]))
    elif kokler == "NoRealRoot":
        print(Fore.LIGHTGREEN_EX+"Denklemin Reel Sayı Kökü Yok.")
    else:
        print(Fore.LIGHTGREEN_EX+"Birinci Kök: {}\nİkinci Kök: {}".format(kokler[0], kokler[1]))
        sleep(3)
















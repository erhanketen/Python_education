print("---Mükemmel Sayı Programı---")

#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def bolenler(x):
    bol = []
    for i in range(1,x):
        if x % i == 0:
            bol.append(i)
    return bol

def muksayı(y):
    a = bolenler(y)
    b = 0
    for i in a:
        b += i
    if b == y:
        return True
    else:
        return False

girdi = int(input("Girdi giriniz: "))
if muksayı(girdi) :
    print("{} sayısı bir mükemmel sayıdır.".format(girdi))
elif not muksayı(girdi) :
    print("{} sayısı bir mükemmel sayı değildir.".format(girdi))












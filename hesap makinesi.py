print("****************************\n\n"
      "       HESAP MAKİNESİ\n\n"
      "****************************")

import math
from math import log,sqrt,sin,cos,tan,asin,acos,atan

print("İşlemler :\nToplama - top\nÇıkartma - cik\nÇarpma - cap\nBölme - bol\nLograritma - log\nKarekök - sqrt\nsinüs -sin\ncosinüs - cos\ntanjant - tan\nTersleri - asin acos atan")

def top():
    sayı0 = int(input("Toplanacak Sayı Girin:"))
    sayı0a = int(input("Toplanacak Sayı Girin:"))
    sayılist = [sayı0, sayı0a]
    a = 1
    while a == 1:
        sayı0b = input("Başka Sayı Varsa Girin, Yoksa 'q'")
        if sayı0b == "q":
            a = 0
        else:
            sayı0b = int(sayı0b)
            sayılist.append(sayı0b)

    x = 0
    for i in sayılist:
        x += i
    return x
def cik():
    sayı0 = int(input("Çıkarılıcak Sayı Girin:"))
    sayı0a = int(input("Çıkartılacak Sayı Girin:"))
    sayılist = [sayı0a]
    a = 1
    while a == 1:
        sayı0b = input("Başka Sayı Varsa Girin, Yoksa 'q'")
        if sayı0b == "q":
            a = 0
        else:
            sayı0b = int(sayı0b)
            sayılist.append(sayı0b)

    x = 0
    for i in sayılist:
        x -= i
    return sayı0 + x
def cap(*a):
    x = 1
    for i in a:
        x *= i
    return x
def bol(*a):
    x = 1
    for i in a:
        x /= i
    return x

while True:
    girdi = input("Yapılacak İşlemi Seçiniz(çıkmak için 'q'):")
    if girdi == "q":
        print("Çıkılıyor...")
        break
    if girdi == "top":
        print("Toplamları = ",top())

    elif girdi == "cik":
        print("Çıkarılmışları = ",cik())











from time import sleep

def calculator():
    girdiler = []
    while True:
        girdi = input("İşlemi Giriniz(çıkmak için =):")
        if girdi == "=":
            print("Hesaplanıyor...")
            sleep(1)
            break
        else:
            girdiler.append(girdi)
    girdilerint = []
    for i in girdiler:
        try:
            i = int(i)
            girdilerint.append(i)
        except ValueError:
            girdilerint.append(i)
    for i in girdilerint:

        if i == "*":
            girdilerint[girdilerint.index(i)+1] = girdilerint[girdilerint.index(i)-1] * girdilerint[girdilerint.index(i)+1]
            girdilerint.pop(girdilerint.index(i))
        elif i == "/":
            girdilerint[girdilerint.index(i)+1] = girdilerint[girdilerint.index(i)-1] / girdilerint[girdilerint.index(i)+1]
            girdilerint.pop(girdilerint.index(i))
        if i == "+":
            girdilerint[girdilerint.index(i)+1] = girdilerint[girdilerint.index(i)-1 ] + girdilerint[girdilerint.index(i)+1]
            girdilerint.pop(girdilerint.index(i))
        elif i == "-":
            girdilerint[girdilerint.index(i) + 1] = girdilerint[girdilerint.index(i) - 1] - girdilerint[girdilerint.index(i) + 1]
            girdilerint.pop(girdilerint.index(i))
    return girdilerint[-1]
print("Açılıyor...")
sleep(1)
print("""
****************************************

             HESAP MAKİNESİ

****************************************
    """)
print("İşleminizin sonucu = {}".format(calculator()))
while True:
    feedback = input("Başka İşlem Yapacak Mısınız?(y/n):")
    if feedback == "y":
        print("İşleminizin sonucu = {}".format(calculator()))
    elif feedback == "n":
        print("Kapatılıyor...")
        break

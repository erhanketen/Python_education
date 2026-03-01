from time import sleep

isim_liste = []
harf_notu = []
isim_not =[]

def dosyaokuma(dosya_yolu):
    with open(dosya_yolu,"r+", encoding="utf-8") as file:
        dosya = file.read()
        dosya = dosya.split(",")
        int_liste = []
        for i in dosya:
            try:
                sayi = int(i)
                int_liste.append(sayi)
            except ValueError:
                isim_liste.append(i)
        isim_liste.pop()
        gruplar = [int_liste[i:i + 3] for i in range(0, len(int_liste), 3)]
        return gruplar

def not_hesapla(dosya_yolu):

    for i in dosyaokuma(dosya_yolu):
        toplam = 0
        for j in i:
            toplam += j
        ortalama = toplam / 3
        if ortalama <= 40:
            harf_notu.append("FF")
        elif 40 < ortalama <= 50:
            harf_notu.append("DD")
        elif 50 < ortalama <= 60:
            harf_notu.append("CC")
        elif 60 < ortalama <= 70:
            harf_notu.append("BB")
        elif 70 < ortalama <= 80:
            harf_notu.append("BA")
        elif 80 < ortalama <= 90:
            harf_notu.append("AA")
        elif 90 < ortalama <= 100:
            harf_notu.append("A+")

    for i in isim_liste:
        isim_not.append(i)
        i = harf_notu[isim_liste.index(i)]
        isim_not.append(i)
#define dosya_yaz():
def dosya_yaz(dosya_yazma_yolu):
    with open(dosya_yazma_yolu,"w+", encoding="utf-8") as file:
        for i in isim_not:
            if len(i) > 2:
                file.write(i)
            else:
                file.write(" --> ")
                file.write(i)
                file.write("\n")


print("""
    ----------------------------------------

            HARF NOTU YAZAN PROGRAM

    ----------------------------------------
    """)
while True:
    try:
        dosya_yolu = input("Hesaplanacak Dosyanın Yolunu Yazınız:")
        print("Hesaplanıyor...")
        not_hesapla(dosya_yolu)
        sleep(1)
        dosya_yazma_yolu = input("Harf Notu Dosyasının Yazılacağı Yolu Yazınız:")
        print("Yazılıyor...")
        dosya_yaz(dosya_yazma_yolu)
        sleep(1.5)
        print("Dosyanız Hazır! Dosya Konumu : {}".format(dosya_yazma_yolu))
        break
    except PermissionError:
        print("Geçerli Bir Dosya Yolu Seçiniz Lütfen!")
        continue





# C:\Users\KETENBTVICTUS\PycharmProjects\PythonProject\eğitim\notlar.txt   --> okunacak dosya
# C:\Users\KETENBTVICTUS\PycharmProjects\PythonProject\eğitim\harf_notlar.txt  --> yazılacak dosya
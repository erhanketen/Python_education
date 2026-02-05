print("-Hesap Makinesi-")


d = 0
while d == 0:
    s1 = int(input("Birinci Sayıyı Giriniz:"))
    s2 = int(input("İkinci Sayıyı Giriniz:"))


    islem = input("Yapılacak İşlemi Seçiniz:")
    a = 1
    while a == 1:
        if islem == "toplama" or islem == "Toplama" or islem == "TOPLAMA":
            cvp = s1+s2
            print("Cevap:",cvp)
            a = 0
        elif islem == "çıkartma" or islem == "Çıkartma" or islem == "ÇIKARTMA":
            cvp = s1-s2
            print("Cevap:",cvp)
            a = 0
        elif islem == "bölme" or islem == "Bölme" or islem == "BÖLME":
            cvp = s1/s2
            print("Cevap:",cvp)
            a = 0
        elif islem == "Çarpma" or islem == "çarpma" or islem == "ÇARPMA":
            cvp = s1*s2
            print("Cevap:",cvp)
            a = 0
        else:
            print("Lütfen Geçerli Bir İşlem Seçiniz")

    onay = input("Başka İşlem Yapacak Mısınız? Y/N:")
    if onay == "Y"or onay == "y":
        d = 0
    elif onay == "N"or onay == "n":
        d = 1
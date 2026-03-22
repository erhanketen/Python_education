from kütüphane_sınıf_DB import *

print(Fore.LIGHTCYAN_EX+"""
----------------------------------------


       KÜTÜPHANE YÖNETİM SİSTEMİ


----------------------------------------

İŞLEMLER:

1-) Kitapları Göster
2-) Kitap Sorgula
3-) Kitap Ekle
4-) Kitap Sil
5-) Baskı Yükselt

Çıkmak İçin 'exit' yazın.
""")

kutuphane = Kutuphane()

while True:
    girdi = input(Fore.RED+"İşlem Numarasını Giriniz:")
    if girdi == "exit":
        kutuphane.baglanti_kes()
        print(Fore.LIGHTWHITE_EX+"Kapatılıyor...")
        sleep(1)
        break
    elif girdi == "1":
        kutuphane.kitap_goster()
    elif girdi == "2":
        isim = input(Fore.LIGHTCYAN_EX+"Kitap İsmini Giriniz:")
        print(Fore.LIGHTWHITE_EX+"Aranıyor...")
        sleep(1)
        kutuphane.kitap_sorgula(isim)
    elif girdi == "3":
        isim = input(Fore.LIGHTCYAN_EX+"Kitap İsmi:")
        yazar = input(Fore.LIGHTCYAN_EX + "Kitap Yazarı:")
        yayinevi = input(Fore.LIGHTCYAN_EX + "Kitap Yayınevi:")
        tur = input(Fore.LIGHTCYAN_EX + "Kitap Türü:")
        baski = int(input(Fore.LIGHTCYAN_EX + "Kitap Baskı Sayısı:"))
        sayfa_sayisi = int(input(Fore.LIGHTCYAN_EX + "Kitap Sayfa Sayısı:"))

        print(Fore.LIGHTWHITE_EX+"Ekleniyor...")
        sleep(1)
        kitap = Kitap(isim,yazar,yayinevi,tur,baski,sayfa_sayisi)
        kutuphane.kitap_ekle(kitap)
        print(Fore.GREEN + "Kitap Eklendi!")
    elif girdi == "4":
        isim = input(Fore.LIGHTCYAN_EX+"Kitap İsmini Giriniz:")
        cevap = input(Fore.LIGHTRED_EX+"Emin misiniz? (y/n):")
        if cevap == "y" or cevap == "Y":
            print(Fore.LIGHTWHITE_EX+"Siliniyor...")
            sleep(1)
            kutuphane.kitap_sil(isim)
            print(Fore.GREEN + "Kitap Silindi!")
        elif cevap == "n" or cevap == "N":
            print(Fore.GREEN+"İşlem İptal Edildi.")
            continue
    elif girdi == "5":
        isim = input(Fore.LIGHTCYAN_EX+"Kitap İsmini Giriniz:")
        print(Fore.LIGHTWHITE_EX+"Baskı Sayısı Yükseltiliyor...")
        sleep(1)
        kutuphane.baski_yukselt(isim)
        print(Fore.GREEN + "Baskı Sayısı Yükseltildi!")
    else:
        print(Fore.RED+"Geçersiz İşlem Numarası Girdiniz!")







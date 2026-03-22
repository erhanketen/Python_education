from DB_Classes import *

giris = Kullanicilar()

while True:
    print(Fore.LIGHTCYAN_EX + """
-----------------------------------------


            KULLANICI GİRİŞİ


-----------------------------------------

İŞLEMLER:

1-) Giriş Yap
2-) Kayıt Ol

Çıkmak İçin 'exit' Yaz
""")

    islem = input(Fore.LIGHTRED_EX+"İşlem Numarasını Giriniz:")

    if islem == "exit":
        print(Fore.LIGHTWHITE_EX+"Kapatılıyor...")
        sleep(1)
        break
    elif islem == "1": #GİRİŞ YAP (kullanici_adi,sifre)
        kullanici_adi = input(Fore.LIGHTWHITE_EX+"Kullanıcı Adınız:")
        sifre = input(Fore.LIGHTWHITE_EX+"Şifreniz:")

        kullanici = giris.giris_yap(kullanici_adi,sifre)
        if not kullanici:
            print(Fore.RED + "Giriş Başarısız!")
        else:
            print(Fore.LIGHTGREEN_EX + "Giriş Başarılı.")

            hesap(giris,kullanici)

    elif islem == "2": #KAYIT OL
        yeni_kayit = kayit()

        print(Fore.LIGHTWHITE_EX,"Kayıt Oluşturuluyor...")
        sleep(2)
        giris.kayit_ol(yeni_kayit)
        print(Fore.LIGHTGREEN_EX+"Kayıt Oluşturuldu!")

    else:
        print(Fore.RED+"Geçersiz Giriş!")





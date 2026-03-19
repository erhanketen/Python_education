from colorama import Fore , init
from time import sleep
from random import randint
init(autoreset=True)

class Kumanda():
    def __init__(self,TV_durum="Kapalı",kanal="TRT",kanal_listesi=["TRT"],kanal_sayısı=1,ses=0):
        self.TV_durum=TV_durum
        self.kanal=kanal
        self.kanal_sayısı = kanal_sayısı
        self.ses=ses
        self.kanal_listesi=kanal_listesi

    def __str__(self):
        return Fore.LIGHTWHITE_EX+"""
        BİLGİLER:
        
        TV Durumu: {}
        Kanal: {}
        Kanal Sayısı: {}
        Ses: {}
        """.format(self.TV_durum,self.kanal,self.kanal_sayısı,self.ses)

    def __len__(self):
        return self.kanal_sayısı

    def ac_kapa(self):
        if self.TV_durum=="Kapalı":
            print("Açılıyor...")
            sleep(2)
            self.TV_durum="Açık"
        elif self.TV_durum=="Açık":
            print("Kapatılıyor...")
            sleep(2)
            self.TV_durum = "Kapalı"

    def kanal_degistir(self):
        if self.kanal_sayısı == 1:
            print("Başka Kanal Yok.")
        else:
            print("KANAL LİSTESİ:")
            kanal_listesi = list(enumerate(self.kanal_listesi))
            for i,j in kanal_listesi:
                print(i+1,j,sep="- ")
            kanal = input("Kanalı Seçiniz:")
            print(kanal_listesi)
            for i,j in kanal_listesi:
                if int(kanal) == i+1:
                    print(Fore.LIGHTWHITE_EX + j)
                    self.kanal = kanal
                    break
            else:
                print(Fore.RED + "Geçersiz Kanal Seçildi!")

    def kanal_ekle(self):
        kanal = input("Kanal Adını Giriniz:")
        if kanal in self.kanal_listesi:
            print(Fore.RED+"Bu kanal zaten mevcut.")
        else:
            print(Fore.LIGHTWHITE_EX+"Kanal Ekleniyor...")
            sleep(2)
            self.kanal_listesi.append(kanal)
            print(Fore.LIGHTWHITE_EX+"Kanal Eklendi.")
            self.kanal_sayısı += 1

    def kanal_sil(self):
        if self.kanal_sayısı == 1:
            print(Fore.RED+"Tek Kanal Var ve bu kanal silinemez!")
        else:
            print("Siliniyor...")
            sleep(2)
            self.kanal_listesi.remove(self.kanal)
            print("Silindi.")
            self.kanal_sayısı -= 1

    def random_kanal(self):
        while True:
            kanal_numara = randint(0,len(self.kanal_listesi)-1)
            if self.kanal_sayısı == 1:
                print(Fore.RED+"Başka Kanal Yok.")
                break
            elif self.kanal_listesi[kanal_numara] == self.kanal:
                continue
            else:
                self.kanal = self.kanal_listesi[kanal_numara]
                print("Mevcut Kanal: {}".format(self.kanal))
                break

    def kanal_listesi_goster(self):
        kanal_listesi1 = enumerate(self.kanal_listesi)
        for i,j in kanal_listesi1:
            print(i+1,j,sep="- ")

    def ses_duzenleme(self):
        print("Mevcut Ses Seviyesi: {}".format(self.ses))
        while True:
            girdi = input("Ses Arttırma: (+)\nSes Azaltma: (-)\n(tamlamak için 'q')")
            if girdi == "q":
                break
            elif girdi == "+":
                if self.ses == 10:
                    print(Fore.RED+"Ses Seviyesi Max'da!")
                else:
                    self.ses += 1
                    print("Ses Seviyesi: {}".format(self.ses))
            elif girdi == "-":
                if self.ses == 0:
                    print(Fore.RED+"Ses Seviyesi Min'de!")
                else:
                    self.ses -= 1
                    print("Ses Seviyesi: {}".format(self.ses))
            else:
                print(Fore.RED+"Geçersiz Giriş!")


kumanda = Kumanda()

print("""
----KUMANDA----
1- Aç/Kapa
2- TV Durum Göster
3- Kanal Sayısı
4- Kanal Listesi
5- Kanal Değiştir
6- Rastgele Kanal Seç
7- Kanal Ekle
8- Kanal Sil
9- Ses Düzenle
""")
while True:
    girdi = input("İşlem Seçin (çıkmak için 'q'):")
    if girdi == "q":
        print(Fore.LIGHTWHITE_EX+"Çıkılıyor...")
        sleep(2)
        break
    elif girdi == "1":
        kumanda.ac_kapa()
    elif girdi == "2":
        print(kumanda)
    elif girdi == "3":
        print(len(kumanda))
    elif girdi == "4":
        kumanda.kanal_listesi_goster()
    elif girdi == "5":
        kumanda.kanal_degistir()
    elif girdi == "6":
        kumanda.random_kanal()
    elif girdi == "7":
        kumanda.kanal_ekle()
    elif girdi == "8":
        kumanda.kanal_sil()
    elif girdi == "9":
        kumanda.ses_duzenleme()
    else:
        print(Fore.RED+"Geçersiz Girdi!")


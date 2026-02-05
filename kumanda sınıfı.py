import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses=0,kanallar=["TRT"],kanal="TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanallar = kanallar
        self.kanal = kanal

    def ac_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Açılıyor..")
            self.tv_durum = "Açık"
        elif self.tv_durum == "Açık":
            print("Kapanıyor..")
            self.tv_durum = "Kapalı"


    def sesdegis(self):
        while True:
            cvp = input("Sesi Arttır : '+' \nSesi Azalt : '-' \n(ayarı tamamlamak için 'q')")
            if cvp == "+" and self.tv_ses != 100:
                self.tv_ses += 10
            elif cvp == "-" and self.tv_ses != 0:
                self.tv_ses -= 10
            elif cvp == "q":
                break

    def kanal_ekle(self,eklenecek_kanal):
        print("{} Kanalı Ekleniyor...".format(eklenecek_kanal))
        time.sleep(1)
        self.kanallar.append(eklenecek_kanal)
        print("Kanal Eklendi!")

    def kanal_sil(self,silinecek_kanal):
        print("{} Kanalı Siliniyor...".format(silinecek_kanal))
        time.sleep(1)
        self.kanallar.pop(self.kanallar.index(silinecek_kanal))

    def kanal_degis(self,gecilecek_kanal):
        self.kanal = gecilecek_kanal

    def __len__(self):
        return len(self.kanallar)

    def __str__(self):
        return "Kanal: {}".format(self.kanal)

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanallar)-1)
        self.kanal = self.kanallar[rastgele]
        print("Şu anki kanal:", self.kanal)

    def ses_goster(self):
        print("Ses: ",self.tv_ses)

kumanda01 = Kumanda()


while True:
    islemler = input("""
        İŞLEMLER

        1-) Güç Düğmesi:
        2-) Ses Ayarı:
        3-) Kanal Ekleme:
        4-) Kanal Sil:
        5-) Kanal degis:
        6-) Rastgele Kanal:
        7-) Mevcut kanal:
        8-) Kanal Listesi:
        9-) Ses Seviyesi:
        """)

    if islemler == "1":
        kumanda01.ac_kapat()
        if kumanda01.tv_durum == "Açık":
            pass
        elif kumanda01.tv_durum == "Kapalı":
            break
    elif islemler == "2":
        kumanda01.sesdegis()
    elif islemler == "3":
        eklenecekkanal =input("Eklenecek Kanal:")
        kumanda01.kanal_ekle(eklenecekkanal)
    elif islemler == "4":
        kumanda01.kanal_sil()
    elif islemler == "5":
        gecilecekkanal = input("Geçilecek Kanal:")
        kumanda01.kanal_degis(gecilecekkanal)
    elif islemler == "6":
        kumanda01.rastgele_kanal()
    elif islemler == "7":
        print(kumanda01)
    elif islemler == "8":
        print(len(kumanda01))
    elif islemler == "9":
        kumanda01.ses_goster()
    else:
        print("Lütfen Geçerli Bir İşlem Yapınız...")











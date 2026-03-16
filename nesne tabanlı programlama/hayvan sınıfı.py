class Hayvan():
    def __init__(self,tur="Bilinmiyor.",cinsi="Bilinmiyor.",ad="Bilinmiyor.",yas="Bilinmiyor.",sahibi="Sahipsiz."):
        self.tur = tur
        self.cinsi = cinsi
        self.ad = ad
        self.yas = yas
        self.sahibi = sahibi

    def __str__(self):
        return """
        Bilgiler:
        
        Türü: {}
        Cinsi: {}
        Adı: {}
        Yaşı: {}
        Sahibi: {} 
        """.format(self.tur,self.cinsi,self.ad,self.yas,self.sahibi)

    def __len__(self):
        return self.yas

class Kedi(Hayvan):
    def sahiplendir(self):
        yeni_sahip = input("Yeni Sahibi Giriniz:")
        self.sahibi = yeni_sahip

class Köpek(Hayvan):
    def __init__(self,asilar="Aşısız.",*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.asilar = asilar

    def __str__(self):
        return """
        Bilgiler:
        
        Türü: {}
        Cinsi: {}
        Adı: {}
        Yaşı: {}
        Sahibi: {} 
        Aşı Durumu: {}
        """.format(self.tur,self.cinsi,self.ad,self.yas,self.sahibi,self.asilar)

    def asi_test(self):
        if self.asilar == "Aşılı":
            return True
        else:
            return False

def yeni_kayit():
    print("Yeni Kayıt Özelliklerini Giriniz (bilinmeyenler boş kalsın):")
    tur = input("Tür:")
    cinsi = input("Cinsi:")
    ad = input("Ad:")
    yas = input("Yas:")
    sahibi = input("Sahibi:")
    if tur == "Kedi":
        kedi = Kedi(tur,cinsi,ad,yas,sahibi)
        return kedi
    elif tur == "Köpek":
        asilar = input("Aşı Durumu:")
        köpek = Köpek(tur,cinsi,ad,yas,sahibi,asilar)
        return köpek

print("""
İŞLEMLER:

1- Yeni Kayit
2- Bilgiler
3- Yaş
4- Aşı Durumu (Köpekler İçin)
""")

while True:
    girdi = input("İşlem Seçiniz (çıkmak için 'exit'):")
    if girdi == "exit":
        break
    elif girdi == "1":
        kayit = yeni_kayit()
        print("Kayıt Oluşturuldu..")
    elif girdi == "2":
        print(kayit)
    elif girdi == "3":
        len(kayit)
    elif girdi == "4":
        try:
            if kayit.asi_test():
                print("Aşıları Tam.")
            else:
                print("Aşısız.")
        except AttributeError:
            print("Aşı Durumu Sadece Köpekler İçin Kontrol Edilebilir.")
    else:
        print("Geçersiz İşlem Seçtiniz!")
"""
Proje 3
Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.


"""

class Hayvan():
    def __init__(self,familya,tür,cins,cinsiyet):
        self.familya=familya
        self.tür = tür
        self.cins = cins
        self.cinsiyet = cinsiyet

    def bilgileri_goster(self):
        print("""
        HAYVAN BİLGİLERİ
        
        Familya: {}
        Tür: {}
        Cins: {}
        Cinsiyet: {}
        
        """.format(self.familya,self.tür,self.cins,self.cinsiyet))


class Köpek(Hayvan):
    def __init__(self,familya,tür,cins,cinsiyet,durum,yaş):
        super().__init__(tür,familya,cins,cinsiyet)
        self.durum = durum
        self.yaş = yaş

    def durumdegistir(self):
        self.durum = input("Köpeğin yeni durmu:")

    def yas_guncelle(self):
        self.yaş = input("Yeni Yaş:")

class Kuş(Hayvan):
    def __init__(self,familya,tür,cins,cinsiyet,renk,habitat):
        super().__init__(familya,tür,cins,cinsiyet)
        self.renk = renk
        self.habitat = habitat

class At(Hayvan):
    def __init__(self,familya,tür,cins,cinsiyet,renk,kullanım_alanı,agırlık):
        super().__init__(familya,tür,cins,cinsiyet)
        self.renk = renk
        self.kullanım_alanı = kullanım_alanı
        self.agırlık = agırlık

    def kullanım_alanı_degistir(self):
        self.kullanım_alanı = input("Yeni Kullanım Alanı:")

    def agırlık_guncelle(self):
        self.agırlık = input("Güncel Ağırlık:")


kopek = Köpek("Memeliler","Köpek","Rotreiver","Erkek","Evcil","12")
kus = Kuş("Kuşlar","Kanarya","Sarı Kanarya","Dişi","Sarı","Ev")
at = At("Memeliler","At","Arap Atı","Erkek","Siyah","Binek",1200)
















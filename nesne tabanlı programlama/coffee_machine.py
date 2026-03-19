from time import sleep
from colorama import Fore , init
init(autoreset=True)

class KahveMakinasi:
    def __init__(self,kahve="SECİLMEDİ",tur="SICAK",aroma="SECİLMEDİ",seker=0,boyut="MID",ucret=0):
        self.kahve = kahve
        self.tur = tur
        self.aroma = aroma
        self.seker = seker
        self.boyut = boyut
        self.ucret = ucret

    def kahve_sec(self):
        print(Fore.LIGHTWHITE_EX+"""
KAHVE TÜRLERİ
        
(1) Espresso ............. 75TL
(2) Türk Kahvesi ......... 90TL
(3) Cafe Latte ........... 120TL
(4) Frappe ............... 160TL
(5) Mocha ................ 170TL
(6) Cappuchino ........... 150TL
(7) Machiato ............. 190TL
        """)
        girdi = input("Kahve Seçiniz:")
        if girdi == "1":
            self.kahve = "Espresso"
            self.ucret += 75
        elif girdi == "2":
            self.kahve = "Türk Kahvesi"
            self.ucret += 90
        elif girdi == "3":
            self.kahve = "Cafe Latte"
            self.ucret += 120
        elif girdi == "4":
            self.kahve = "Frappe"
            self.ucret += 160
        elif girdi == "5":
            self.kahve = "Mocha"
            self.ucret += 170
        elif girdi == "6":
            self.kahve = "Cappuchino"
            self.ucret += 150
        elif girdi == "7":
            self.kahve = "Machiato"
            self.ucret += 190
        else:
            print(Fore.RED+"Geçersiz Girdi!")

    def tur_sec(self):
        print(Fore.LIGHTWHITE_EX+"""
TÜRLER
        
(1) Sıcak
(2) Soğuk
        """)
        girdi = input("Tür Seçiniz:")

        if girdi == "1":
            self.tur = "Sıcak"
        elif girdi == "2":
            self.tur = "Soğuk"
        else:
            print(Fore.RED+"Geçersiz Girdi!")

    def aroma_sec(self):
        print(Fore.LIGHTWHITE_EX+"""
AROMALAR
        
(0) Aroma İstemiyorum ........ +0TL
(1) Çikolata ................. +50TL
(2) Krema .................... +35TL
(3) Karamel .................. +45TL
(4) Krem Şanti ............... +60TL
(5) Fındık ................... +85TL
(6) Ekstra Shot .............. +90TL
        """)

        girdiler=list()
        nums = ("0","1","2","3","4","5","6")

        while True:
            girdi = input("Aroma Seçiniz (Tamamlamak İçin 'ok'):")
            if girdi == "ok":
                break
            elif girdi == "0":
                return None
            elif girdi in girdiler:
                print(Fore.RED+"Bu Aroma Zaten Var!")
            elif girdi in nums:
                girdiler.append(girdi)

        aroma = list()

        for i in girdiler:
            if i == "1":
                aroma.append("Çikolata")
                self.ucret += 50
            elif i == "2":
                aroma.append("Krema")
                self.ucret += 35
            elif i == "3":
                aroma.append("Karamel")
                self.ucret += 45
            elif i == "4":
                aroma.append("Krem Şanti")
                self.ucret += 60
            elif i == "5":
                aroma.append("Fındık")
                self.ucret += 85
            elif i == "6":
                aroma.append("Ekstra Shot")
                self.ucret += 90

        self.aroma = ""
        for i in aroma:
            self.aroma += i
            self.aroma += ", "

    def seker_sec(self):
        try:
            girdi = int(input("Şeker Sayısını Yazın:"))
            self.seker += girdi
        except ValueError:
            print(Fore.RED+"Geçersiz Girdi!")

    def boyut_sec(self):
        print(Fore.LIGHTWHITE_EX+"""
BOYUTLAR
        
(1) Küçük .......... +0Tl
(2) Orta ........... +25TL
(3) Büyük .......... +45Tl
        """)
        girdi = input("Boyut Seçiniz:")
        if girdi == "1":
            self.boyut = "Küçük"
        elif girdi == "2":
            self.boyut = "Orta"
            self.ucret += 25
        elif girdi == "3":
            self.boyut = "Büyük"
            self.ucret += 45
        else:
            print(Fore.RED+"Geçersiz Girdi!")

    def __str__(self):
        return Fore.LIGHTWHITE_EX+"""
SİPARİŞ
        
Kahve: {}
Tür: {}
Aroma(lar): {}
Şeker: {}
Boyut: {}
        
Toplam Ücret: {}TL
        """.format(self.kahve, self.tur, self.aroma, self.seker , self.boyut , self.ucret)

siparis = KahveMakinasi()

print(Fore.LIGHTBLUE_EX+"""
----------------------------------

          KAHVE MAKİNASI

----------------------------------
""")

while True:
    siparis.kahve_sec()
    siparis.tur_sec()
    siparis.aroma_sec()
    siparis.seker_sec()
    siparis.boyut_sec()

    print(siparis)

    feedback = input("Siparişi Onaylıyor musunuz?(y/n)")

    if feedback == "y" or feedback == "Y":
        print(Fore.LIGHTGREEN_EX+"Sipariş Hazırlanıyor...")
        sleep(5)
        print(Fore.LIGHTWHITE_EX+"Afiyet Olsun.")
        break
    elif feedback == "n" or feedback == "N":
        continue
    else:
        print(Fore.RED+"Geçersiz Girdi!")








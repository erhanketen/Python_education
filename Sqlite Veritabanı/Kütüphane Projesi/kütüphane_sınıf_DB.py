from sqlite3 import connect
from time import sleep
from colorama import Fore , init
init(autoreset=True)

class Kitap:
    def __init__(self,isim,yazar,yayinevi,tur,baski,sayfa_sayisi):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return Fore.LIGHTWHITE_EX+"""
KİTAP BİLGİLERİ:
        
Kitap İsmi: {}
Yazar: {}
Yayinevi: {}
Türü: {}
Baskı : {}
Sayfa Sayisi: {}
        """.format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski,self.sayfa_sayisi)

class Kutuphane:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.con = connect("Kütüphane.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitaplar (
        isim TEXT,
        yazar TEXT,
        yayinevi TEXT,
        tur TEXT,
        baski INTEGER,
        sayfa_sayisi INTEGER
        );
        """)
        self.con.commit()

    def baglanti_kes(self):
        self.con.close()

    def kitap_goster(self):
        self.cursor.execute("""
        SELECT * FROM kitaplar;
        """)
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(Fore.RED+"Kütüphanede Hiç Kitap Bulunmuyor.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap)

    def kitap_sorgula(self,isim):
        self.cursor.execute("""
        SELECT * FROM kitaplar WHERE isim = ?;
        """,(isim,))

        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print(Fore.RED+"Bu Kitap Bulunmuyor.")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5])
                print(kitap)
    def kitap_ekle(self,kitap):
        self.cursor.execute("""
        INSERT INTO kitaplar VALUES(?,?,?,?,?,?);
        """,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski,kitap.sayfa_sayisi))
        self.con.commit()

    def kitap_sil(self,isim):
        self.cursor.execute("""
        DELETE FROM kitaplar WHERE isim = ?;
        """,(isim,))
        self.con.commit()

    def baski_yukselt(self,isim):
        self.cursor.execute("""
        SELECT baski FROM kitaplar WHERE isim = ?;
        """,(isim,))

        baski = self.cursor.fetchall()
        baski_sayisi = baski[0][0]

        baski_sayisi += 1

        self.cursor.execute("""
        UPDATE kitaplar SET baski = ? WHERE isim = ?;
        """,(baski_sayisi,isim))
        self.con.commit()



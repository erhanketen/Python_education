from sqlite3 import connect
from time import sleep
from colorama import Fore , init
init(autoreset=True)

class Kullanici:
    def __init__(self,isim,soyisim,kullanici_adi,eposta,tel_no,sifre):
        self.isim = isim
        self.soyisim = soyisim
        self.kullanici_adi = kullanici_adi
        self.eposta = eposta
        self.tel_no = tel_no
        self.sifre = sifre

    def __str__(self):
        return Fore.LIGHTWHITE_EX+"""
        KULLANICI BİLGİLERİ:
        
        İsim: {}
        Soyisim: {}
        Kullanıcı Adı: {}
        Eposta: {}
        Telefon Numarası: {}
        """.format(self.isim,self.soyisim,self.kullanici_adi,self.eposta,self.tel_no)

class Kullanicilar:
    def __init__(self):
        self.con = connect("Kullanıcılar.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar 
        (
        İsim TEXT,
        Soyisim TEXT,
        Kullanıcı_adı TEXT,
        eposta TEXT,
        Telno TEXT,
        Şifre TEXT
        );
        """)
        self.con.commit()

    def baglanti_kes(self):

        self.con.close()

    def giris_yap(self,kullanici_adi,sifre):

        self.cursor.execute("""
        SELECT * FROM kullanicilar WHERE Kullanıcı_adı = ? AND Şifre = ?; 
        """, (kullanici_adi,sifre))

        giris = self.cursor.fetchall()

        if not giris:
            return False
        else:
            for i in giris:
                kullanici = Kullanici(i[0],i[1],i[2],i[3],i[4],i[5])
                return kullanici

    def hesap_bilgisi(self,kullanici):

        self.cursor.execute("""
        SELECT * FROM kullanicilar WHERE Kullanıcı_adı=?
        """, (kullanici.kullanici_adi,))

        bilgiler = self.cursor.fetchall()

        for i in bilgiler:
            kullanici_bilgi = Kullanici(i[0],i[1],i[2],i[3],i[4],i[5])
            print(kullanici_bilgi)

    def kayit_ol(self,kullanici):

        self.cursor.execute("""
        INSERT INTO kullanicilar VALUES (?,?,?,?,?,?);
        """,(kullanici.isim,kullanici.soyisim,kullanici.kullanici_adi,kullanici.eposta,kullanici.tel_no,kullanici.sifre))

        self.con.commit()

    def hesap_sil(self,kullanici):

        self.cursor.execute("""
        DELETE FROM kullanicilar WHERE Kullanıcı_adı=?;
        """, (kullanici.kullanici_adi,))

        self.con.commit()

    def bilgi_guncelle(self,kullanici,islem,yeni_veri):

        if islem == "1":
            self.cursor.execute("""
            UPDATE kullanicilar SET Kullanıcı_adı = ? WHERE Kullanıcı_adı = ?;
            """,(yeni_veri,kullanici.kullanici_adi))
            self.con.commit()
        elif islem == "2":
            self.cursor.execute("""
            UPDATE kullanicilar SET Şifre = ? WHERE Şifre = ?;
            """, (yeni_veri, kullanici.sifre))
            self.con.commit()
        else:
            print(Fore.RED+"Geçersiz İşlem Seçtiniz!")

def hesap(giris,kullanici):
    print(Fore.LIGHTCYAN_EX + """
-------------------------
    
        HOŞGELDİNİZ                               
    
-------------------------                        
    
İŞLEMLER:
    
1-) Hesap Bilgilerini Gör
2-) Bilgilerini Güncelle                        
3-) Hesabı Sil                        
4-) Çıkış Yap                                                       
""")
    while True:
        islem = input(Fore.LIGHTRED_EX + "İşlem Numarasını Giriniz:")

        if islem == "1":
            giris.hesap_bilgisi(kullanici)
        elif islem == "2":
            islem = input(Fore.LIGHTRED_EX + "Kullanıcı Adını Güncelle(1)\n"
                                             "Şifreyi Güncelle (2)\n"
                                             "Seçim:")

            yeni_veri = input(Fore.LIGHTWHITE_EX+"Yeni Bilgi:")

            print(Fore.LIGHTWHITE_EX + "Bilgiler Güncelleniyor...")
            sleep(1)
            giris.bilgi_guncelle(kullanici, islem, yeni_veri)
            print(Fore.LIGHTGREEN_EX+"Bilgiler Güncellendi!")
        elif islem == "3":
            print(Fore.LIGHTWHITE_EX + "Siliniyor...")
            sleep(1)
            giris.hesap_sil(kullanici)
            print(Fore.LIGHTGREEN_EX + "Silindi!")
            break
        elif islem == "4":
            print(Fore.LIGHTWHITE_EX + "Çıkış Yapılıyor...")
            sleep(1)
            break

def kayit():
    isim = input("İsim:")
    soyisim = input("Soyisim:")
    kullanici_adi = input("Kullanıcı Adı:")
    eposta = input("Eposta:")
    tel_no = input("Telefon Numarası:")
    sifre = input("Şifre:")

    yeni_kullanici = Kullanici(isim,soyisim,kullanici_adi,eposta,tel_no,sifre)

    return yeni_kullanici

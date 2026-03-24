import sqlite3

con = sqlite3.connect("../Kütüphane Projesi/Kütüphane.db")

cursor = con.cursor()


def tablo_oluştur():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kitaplik
    (
    İsim TEXT,
    Yazar TEXT,
    Yayınevi TEXT,
    Sayfa_sayisi INTEGER 
    );
    """)
    con.commit()

def veri_ekle():
    cursor.execute("""
    INSERT into kitaplik Values
    (
    'İstanbul Hatırası',
    'Ahmet Ümit',
    'Everest',
    561
    );
    """)
    con.commit()

def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("""
    INSERT into kitaplik Values(?,?,?,?);  
    """,(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def veri_cek():
    cursor.execute("""
    SELECT * FROM kitaplik;    
    """)
    liste = cursor.fetchall()

    print("KİTAPLIK BİLGİLERİ:")

    for i in liste:
        print(i)

def veri_cek2():
    cursor.execute("""
    SELECT İsim,Yazar FROM kitaplik;    
    """)
    liste = cursor.fetchall()

    print("KİTAPLIK BİLGİLERİ:")

    for i in liste:
        print(i)

def veri_cek3(yayinevi):
    cursor.execute("""
    SELECT * FROM kitaplik WHERE Yayınevi = ?;     
    """,(yayinevi,))
    liste = cursor.fetchall()

    print("KİTAPLIK BİLGİLERİ:")

    for i in liste:
        print(i)

def veri_guncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("""
    UPDATE kitaplik SET Yayınevi = ? WHERE Yayınevi = ?;
    """,(yeni_yayinevi,eski_yayinevi))
    con.commit()

def veri_sil(yazar):
    cursor.execute("""
    DELETE FROM kitaplik WHERE Yazar = ?;
    """,(yazar,))
    con.commit()

veri_cek()

con.close()







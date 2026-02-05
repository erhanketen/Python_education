print("-Kullanıcı Girişi-")

ad= list(input("Adınız:"))
ad.append(" ")
soyad = list(input("Soyadınız:"))
TC = input("TC Kimlik Numaranız:")
sifre = input("Sifreniz:")

print("Bilgileriniz Kaydedildi...")
print("Lütfen Giriş Yapınız...")

a=1
while a==1:

    giris = list(input("Ad ve Soyadınız:"))
    giris1 = input("TC Kimlik Numaranız:")
    giris2 = input("Şifreniz:")

    if giris == ad+soyad and giris1==TC and giris2==sifre:
        print("Giriş Başarılı...")
        a=0
    elif giris != ad+soyad and giris1==TC and giris2==sifre:
        print("Ad ve Soyadınız Hatalı.. ")
        print("Tekrar Deneyiniz...")
    elif giris == ad+soyad and giris1!=TC and giris2==sifre:
        print("TC Kimlik Numaranız Hatalı..")
        print("Tekrar Deneyiniz...")
    elif giris == ad+soyad and giris1==TC and giris2!=sifre:
        print("Şifreniz Hatalı..")
        print("Tekrar Deneyiniz...")
    elif giris != ad+soyad and giris1!=TC and giris2==sifre:
        print("Ad-Soyadınız ve TC kimlik Numaranız Hatalı...")
        print("Tekrar Deneyiniz...")
    elif giris != ad+soyad and giris1==TC and giris2!=sifre:
        print("Ad-Soyadınız ve Şifreniz Hatalı..")
        print("Tekrar Deneyiniz...")
    elif giris == ad+soyad and giris1!=TC and giris2!=sifre:
        print("TC Kimlik NUmaranız ve Şifreniz Hatalı..")
        print("Tekrar Deneyiniz...")

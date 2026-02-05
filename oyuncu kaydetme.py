print("Oyuncu Kaydetme Programı")

ad = input("İsminiz:")
soyad = input("Soyadınız:")
dogum = input("Doğum Tarihiniz:")
spor = input("İlgilendiğiniz Spor Dalı:")

oyuncu = [ad,soyad,dogum,spor,]

print("İsminiz: {} \nSoyadınız: {} \nDoğum Tarihiniz: {} \nİlgilendiğiniz Spor Dalı: {}  ".format(oyuncu[0],oyuncu[1],oyuncu[2],oyuncu[3]))

onay = input("Bilgilerin Doğruluğunu Onaylıyor musunuz? Y/N:")

if onay == "Y" or onay == "y":
    print("Bilgileriniz Kaydedildi...")
else:
    print("Lütfen Bilgilerinizi Tekrar Girin..")
    while onay == "N" or onay == "n":
        ad = input("İsminiz:")
        soyad = input("Soyadınız:")
        dogum = input("Doğum Tarihiniz:")
        spor = input("İlgilendiğiniz Spor Dalı:")
        oyuncu = [ad, soyad, dogum, spor]
        print("İsminiz: {} \nSoyadınız: {} \nDoğum Tarihiniz: {} \nİlgilendiğiniz Spor Dalı: {}  ".format(oyuncu[0],oyuncu[1],oyuncu[2],oyuncu[3]))

        onay = input("Bilgilerin Doğruluğunu Onaylıyor musunuz? Y/N:")

print("Bilgileriniz Kaydedildi...")


kullanıcıadı = input("Lütfen Kullanıcı Adınızı Belirleyiniz:")

print("Kullanıcı Adınız Kaydedildi...")

sifre =  int(input("Lütfen 4 Haneli Parolanızı Belirleyin:"))

print("Şifreniz Kaydedildi..")

print("Lütfen Giriş Yapın")


a = 0
while a == 0:
    kullanıcı = input("Kullanıcı Adınızı Giriniz:")
    sifreo = int(input("Şifrenizi Giriniz:"))
    if kullanıcı == kullanıcıadı and sifreo == sifre:
        print("Giriş Başarılı..")
        a = 1
    elif kullanıcı == kullanıcıadı and not sifreo == sifre:
        print("Şifreniz Yanlış Lütfen Tekrar Deneyiniz..")
        sifredegis = input("Şifrenizi Unuttuysanız Değiştirmek İstiyor musunuz? Y/N:")
        if sifredegis == "Y" or sifredegis == "y":
            sifre2 = int(input("Yeni 4 Haneli Şifrenizi Giriniz:"))
            sifre = sifre2
            print("Yeni Şifreniz Kaydedildi.\nGiriş Yapmaya Dönülüyor...")
        else:
            print("Giriş Yapmaya Dönülüyor...")
    elif not kullanıcı == kullanıcıadı and sifreo == sifre:
        print("Kullanıcı Adı Yanlış Lütfen Tekrar Deneyiniz..")
    else:
        print("Kullanıcı Adı ve Şifre Yanlış Lütfen Tekrar Deneyiniz..")













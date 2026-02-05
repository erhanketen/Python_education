print("-ÜÇGEN-DİKDÖRTGEN BELİRLEME-")

islem = input("Lütfen İşlemi seçin:")
if islem == "Dörtgen" or islem == "dörtgen" or islem == "DÖRTGEN":
    print("Dört Kenar Uzunluğunu Giriniz:")
    s1 = input("Kenar 1:")
    s2 = input("Kenar 2:")
    s3 = input("Kenar 3:")
    s4 = input("Kenar 4:")
    if s1 == s2 == s3 == s4:
        print("Bu dörtgen bir karedir..")
    elif s1 == s2 and s3 == s4 and s1 != s3 and s1 !=s4 and s2 != s3 and s1!= s4:
        print("Bu dörtgen bir dikdörtgendir..")
    else:
        print("Bu sıradan bir dörtgendir..")
elif islem == "Üçgen" or islem == "ÜÇGEN" or islem== "üçgen":
    print("Üç Kenar Uzunluğu Giriniz:")
    s1 = input("Kenar 1:")
    s2 = input("Kenar 2:")
    s3 = input("Kenar 3:")
    if s1 == s2 == s3:
        print("Bu bir Eşkenar üçgendir..")
    elif (s1 == s2 and s3 != s1 and s3 != s2) or (s1 == s3 and s2 != s1 and s2 != s3) or (s2 == s3 and s1 != s2 and s1 != s3):
        print("Bu bir İkizkenar Ügendir..")
    elif s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
        print("Bu sıradan bir üçgendir...")
    else:
        print("Bu kenar uzunlukları bir üçgen belirtmez..")


print("**********************************************\n\n"
      
                     "                ASAL SAYI BULMA\n\n"
      
      "**********************************************")


def asal(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True


while True:
    girdi = input("Sayıyı Girin(Çıkmak İçin q):")
    if girdi == "q":
        print("Programdan Çıkılıyor...")
        break
    else:
        girdi = int(girdi)
        if asal(girdi):
            print("{} sayısı bir asal sayıdır.".format(girdi))
        else:
            print("{} sayısı bir asal sayı değildir.".format(girdi))












print("************************************************\n\n"
      "               PERMÜTASYON HESAPLAMA\n\n"
      "************************************************")

def fakto(x):
    faktoriel = 1
    if x == 0 or x == 1:
        return faktoriel
    else:
        for i in range(2,x+1):
            faktoriel *= i
        return faktoriel

permutasyon = lambda n,r : fakto(n)/fakto(n-r)

while True:
    sayı1 = int(input("Kümedeki Toplam Eleman Sayısı:"))
    sayı2 = int(input("Seçilecek Eleman Sayısı:"))

    print("{} elemanlı bir kümeden {} elemanlı permütasyon: {}".format(sayı1,sayı2,permutasyon(sayı1,sayı2)))

    girdi = input("Başka Hesap?(Y/N):")
    if girdi == "Y" or girdi == "y":
        continue
    elif girdi == "N" or girdi == "n":
        print("Program Bitiriliyor...")
        break
    else:
        print("Geçerli Bir Cevap Giriniz..")
        continue














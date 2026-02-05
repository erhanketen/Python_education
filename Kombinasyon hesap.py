

print("************************************************\n\n"
      "               KOMBİNASYON HESAPLAMA\n\n"
      "************************************************")

def fakto(x):
    faktoriel = 1
    if x == 0 or x == 1:
        return faktoriel
    else:
        for i in range(2,x+1):
            faktoriel *= i
        return faktoriel

kombinasyon = lambda n,r : fakto(n)/(fakto(r)*fakto(n-r))


while True:
    sayı1 = int(input("SAyı:"))
    sayı2 = int(input("Sayı:"))

    print("{} sayısının {}'lı kombinasyonu: {}".format(sayı1,sayı2,kombinasyon(sayı1,sayı2)))
    girdi = input("Girdi(Y/N):")
    if girdi == "Y"or girdi == "y":
        continue
    elif girdi == "N"or girdi == "n":
        print("Program Sonlandırılıyor...")
        break
    else:
        print("Geçerli Bişe Gir")






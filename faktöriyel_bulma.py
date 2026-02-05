print("--Faktöriyel Bulma Programı--")
# 7 }  1 2 3 4 5 6 7



sayi = int(input("Sayıyı Giriniz:"))
liste = list(range(1,sayi+1))
a = 1


for i in liste:
    a = a*i


print("{}! = {}".format(sayi,a))


print("İkinci Dereceden Bir Bilinmeyenli Bir Denklemin Köklerini Bulma")

a = int(input("Denklemin Baş Katsayısını Giriniz:"))
b = int(input("Denkleimin x'li Teminin Katsayısını Giriniz"))
c = int(input("Denklemin Sabit Sayısını Giriniz"))

katsayilar = [a,b,c]

delta = b**2 - (4* a * c)

x1 = (-b + delta** 0.5) / (2*a)
x2 = (-b - delta** 0.5) / (2*a)

print("Denklemin Kökleri {} ve {} dir.".format(x1,x2))


# (x+1)^2 = x^2 + 2x + 1 /// x^2+5x+6 x1 = -3 x2 = -2
# kökleri --> x1 = -1 ve x2 = -1



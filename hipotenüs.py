print("Hipotenüs Hesaplama")

# x^2 = y^2 + z^2 --> x = (Y^2 + z^2)^1/2

y = int(input("Lütfen Kenar Uzunluğu Giriniz:"))
z = int(input("Lütfen Diğer Kenar Uzunluğunu Giriniz:"))

hipotenus = (y**2 + z**2)**(1/2)

print("Hipotenus:",int(hipotenus))



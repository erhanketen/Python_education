
def ekstra(func):
    def wrapper(sayilar):
        mukemmel_sayilar = list()
        for sayi in sayilar:
            bolenler = []
            toplam = 0
            for i in range(1,sayi):
                if sayi % i == 0:
                    bolenler.append(i)
            for i in bolenler:
                toplam += i

            if sayi == toplam:
                mukemmel_sayilar.append(sayi)
        print("Mükemmel Sayılar")
        for i in mukemmel_sayilar:
            print(i)

        func(sayilar)

    return wrapper


@ekstra
def asal(sayilar):

    asallar = list()

    for sayi in sayilar:
        if sayi == 2:
            asallar.append(sayi)
        else:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                asallar.append(sayi)
    print("Asal Sayilar:")
    for i in asallar:
        print(i)

asal(range(1,100))











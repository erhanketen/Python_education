
def decorator(func):
    def wrapper(sayilar):
        cifler_toplam = 0
        tekler_toplam = 0
        cif_tek = {"cif":0,"tek":0}

        for i in sayilar:
            if i % 2 == 0:
                cifler_toplam += i
                cif_tek["cif"] += 1
            else:
                tekler_toplam += i
                cif_tek["tek"] += 1

        ciftler_ort = cifler_toplam / cif_tek["cif"]
        tekler_ort = tekler_toplam / cif_tek["tek"]

        func(sayilar)
        print("Çiftlerin Ortalaması:",ciftler_ort)
        print("Teklerin Ortalaması:",tekler_ort)
    return wrapper

@decorator
def ortalama_al(sayilar):

    toplam = 0
    for i in sayilar:
        toplam += i

    print("Ortalama:",toplam/len(sayilar))

ortalama_al([10,12,1,18,13,15,19])






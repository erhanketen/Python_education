#"C:\\Users\\KETENBTVICTUS\\PycharmProjects\\PythonProject\\Python_education\\txt dosyaları\\metin.txt"

class Metin:

    def __init__(self,dosya_yolu):

        self.dosya_yolu = dosya_yolu
        self.kelimeler = []

        with open(self.dosya_yolu,'r',encoding="utf-8") as file:
            file = file.read()
            file = file.split()

            for i in file:
                i = i.removesuffix(".")
                i = i.removesuffix(",")
                self.kelimeler.append(i)

    def kelime_sayisi(self):

        self.kelime_sayisi = dict()

        for i in self.kelimeler:
            if i in self.kelime_sayisi:
                self.kelime_sayisi[i] += 1
            else:
                self.kelime_sayisi[i] = 1

        for i in self.kelime_sayisi.keys():
            print(i,self.kelime_sayisi[i])

    def arama(self,kelime):

        kelimeler = self.kelimeler
        aranan = dict()
        indx = list()

        for i in kelimeler:
            ind = kelimeler.index(i)
            if i in aranan:
                aranan[i] += 1
                indx.append(ind+1)
                kelimeler.remove(i)
                kelimeler.insert(ind,i[::-1])
            elif i == kelime:
                aranan[i] = 1
                indx.append(ind+1)
                kelimeler.remove(i)
                kelimeler.insert(ind,i[::-1])

        if not aranan:
            return "NotFoundError"

        print("'{}' kelimesi, metinde {} kere geçiyor.".format(kelime,aranan[kelime]))

        i = 0
        while i < aranan[kelime]:
            print("{}. kelime".format(indx[i]))
            i += 1



metin = Metin("C:\\Users\\KETENBTVICTUS\\PycharmProjects\\PythonProject\\Python_education\\txt dosyaları\\metin.txt")

metin.arama("Victor")









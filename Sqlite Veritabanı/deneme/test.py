class Kullanici:
    def __init__(self,isim,yazar,yayinevi):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi

    def __str__(self):
        return """
        {}
        {}
        {}
        """.format(self.isim,self.yazar,self.yayinevi)

    def veri_cek(self):
        isim = "erhan"
        yazar = "ben"
        yayinevi = "biri"

        bise = (self.isim,self.yazar,self.yayinevi)
        ise = (isim,yazar,yayinevi)

        zipped = zip(bise,ise)

        for i,j in zipped:
            i = j

        return self

biri = Kullanici("e","a","b")

print(biri.veri_cek())
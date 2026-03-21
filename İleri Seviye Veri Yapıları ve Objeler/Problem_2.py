"""
Problem 2
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.
"""

def agrostis(dosya_yolu):
    with open(dosya_yolu, 'r' , encoding="utf-8") as file:

        file = file.readlines()
        agrostis_kelime = str()

        for i in file:
            agrostis_kelime += i[0]

        print(agrostis_kelime)

agrostis("C:\\Users\\KETENBTVICTUS\\PycharmProjects\\PythonProject\\Python_education\\txt dosyaları\\siir.txt")



# "C:\\Users\\KETENBTVICTUS\\PycharmProjects\\PythonProject\\Python_education\\txt dosyaları\\siir.txt"



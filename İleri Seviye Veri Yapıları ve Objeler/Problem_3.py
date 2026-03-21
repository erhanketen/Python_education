"""
Problem 3
Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun.
Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.
"""

def kontroller(dosya_yolu):

    gecerli = {"gmail.com","yahoo.com","hotmail.com"}

    with open(dosya_yolu, 'r', encoding="utf-8") as file:

        file = file.readlines()
        gecerliler = []

        for i in file:

            i = i.strip('\n')

            if i[i.find("@") + 1:] in gecerli:
                gecerliler.append(i)
            elif i[i.find("@") + 1:] in gecerli:
                gecerliler.append(i)
            elif i[i.find("@") + 1:] in gecerli:
                gecerliler.append(i)

        for i in gecerliler:
            print(i)

kontroller("C:\\Users\\KETENBTVICTUS\\PycharmProjects\\PythonProject\\Python_education\\txt dosyaları\\mailler.txt")
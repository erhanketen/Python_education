print("Tam Bölen Bulma Programı")

def tambul(x):
    bölenler = [1,x]
    for i in range(2,x):
        if x % i == 0:
            bölenler.append(i)
    bölenler.sort()
    return bölenler


while True:
    girdi = input("Bir Sayı Giriniz (çıkmak için 'q'):")
    if girdi == "q":
        print("Programdan Çıkılıyor..")
        break
    else:
        girdi = int(girdi)
        print("{} sayısının bölenleri {}'dir.".format(girdi,tambul(girdi)))












from time import sleep
from colorama import Fore , init
init(autoreset=True)

def dosya_okuma(dosya_yolu):
    with open(dosya_yolu,"r+",encoding="utf-8") as file:
        dosya = []
        oyuncular = []
        file = file.read()
        file = file.split("\n")
        for i in file:
            dosya.append(i)
        for i in dosya:
            i  = i.split(",")
            oyuncular.append(i)
        return oyuncular

def dosya_yazma(dosya_yolu,dosya_yazma_yolu_gs,dosya_yazma_yolu_bjk,dosya_yazma_yolu_fb):

    gs_list = []
    bjk_list = []
    fb_list = []

    for i,j in dosya_okuma(dosya_yolu):
        if "Galatasaray" in j:
            gs_list.append(i)
        elif "Beşiktaş" in j:
            bjk_list.append(i)
        elif "Fenerbahçe" in j:
            fb_list.append(i)

    with open(dosya_yazma_yolu_gs, "w" , encoding = "utf-8") as file:
        for i in gs_list:
            file.write(i)
    with open(dosya_yazma_yolu_bjk, "w" , encoding = "utf-8") as file:
        for i in bjk_list:
            file.write(i)
    with open(dosya_yazma_yolu_fb, "w" , encoding = "utf-8") as file:
        for i in fb_list:
            file.write(i)

print(Fore.MAGENTA+"""
------------------------------------------------

              TAKIM AYIRAN PROGRAM

------------------------------------------------
""")

while True:
    try:
        okuma = input("Okunacak Dosyanın Yolunu Giriniz:")
        dosya_okuma(okuma)
        print("Okunuyor...")
        sleep(0.5)
        yazma1 = input("Galatasaray Dosyasının Yazılacağı Yolu Giriniz:")
        yazma2 = input("Beşiktaş Dosyasının Yazılacağı Yolu Giriniz:")
        yazma3 = input("Fenerbahçe Dosyasının Yazılacağı Yolu Giriniz:")
        print("Yazılıyor...")
        dosya_yazma(okuma,yazma1,yazma2,yazma3)
        sleep(1.5)
        print(Fore.GREEN+"Dosyanız Oluşturuldu!\n"
                         "Galatasaray Dosyanın Konumu: {}\n"
                         "Beşiktaş Dosyanın Konumu: {}\n"
                         "Fenerbahçe Dosyanın Konumu: {}\n".format(yazma1,yazma2,yazma3))
        break
    except FileNotFoundError:
        print(Fore.RED+"Dosya Bulunamadı!")
        continue


#txt dosyaları\futbolcular.txt   --> okunacak dosya
#txt dosyaları\gs.txt-fb.txt-bjk.txt   ---> yazılacak dosyalar
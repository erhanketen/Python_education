import math
# FONKSİYON DENEMESİ
liste = [12,"+",20,"sqrt","cos",0]

a = 0
while a < len(liste):
    print("döngü")
    for i in liste:
        indx = liste.index(i)
        if i == "sqrt":
            if liste[indx+1] == "cos":
                pass
            else:
                liste[indx] = math.sqrt(liste[indx+1])
                print("sqrt çalıştı.",liste[indx])
        elif i == "cos":
            if liste[indx+1] == "sqrt":
                pass
            else:
                liste[indx] = math.cos(liste[indx+1])
                print("cos çalıştı.",liste[indx])

    a += 1

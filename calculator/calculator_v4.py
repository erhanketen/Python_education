
girdiler = []
girdiler_int = []

def girdi_al():
    while True:
        girdi = input("İşlemleri Girin:")
        if girdi == "=":
            break
        else:
            girdiler.append(girdi)

    for i in girdiler:
        try:
            i = int(i)
            girdiler_int.append(i)
        except ValueError:
            try:
                i = float(i)
                girdiler_int.append(i)
            except ValueError:
                girdiler_int.append(i)


def hesapla():
    for i in girdiler_int:
        if i == "*":
            girdiler_int[girdiler_int.index("*") + 1] = girdiler_int[girdiler_int.index("*") - 1] * girdiler_int[girdiler_int.index("*") + 1]
            girdiler_int.pop(girdiler_int.index("*"))
        elif i == "/":
            girdiler_int[girdiler_int.index("/") + 1] = girdiler_int[girdiler_int.index("/") - 1] / girdiler_int[girdiler_int.index("/") + 1]
            girdiler_int.pop(girdiler_int.index("/"))
        elif i == "+":
            girdiler_int[girdiler_int.index("+")+1] =  girdiler_int[girdiler_int.index("+")-1] + girdiler_int[girdiler_int.index("+")+1]
            girdiler_int.pop(girdiler_int.index("+"))
        elif i == "-":
            girdiler_int[girdiler_int.index("-") + 1] = girdiler_int[girdiler_int.index("-") - 1] - girdiler_int[girdiler_int.index("-") + 1]
            girdiler_int.pop(girdiler_int.index("-"))
        elif type(i) == float or type(i) == int:
            pass
        else:
            print("Kullandığınız İşlem Geçerli Değil...")
    return girdiler_int[-1]






girdi_al()
print(hesapla())
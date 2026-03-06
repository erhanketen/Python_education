def islemler():
    girdiler = []
    while True:
        girdi = input("İşlem (çıkmak için =):")
        if girdi == "=":
            break
        else:
            girdiler.append(girdi)
    girdilerint = []
    for i in girdiler:
        try:
            i = int(i)
            girdilerint.append(i)
        except ValueError:
            girdilerint.append(i)
    for i in girdilerint:
        if i == "+":
            girdilerint[girdilerint.index(i)+1] = girdilerint[girdilerint.index(i)+1] + girdilerint[girdilerint.index(i)-1]
            girdilerint.pop(girdilerint.index(i))
        elif i == "-":
            girdilerint[girdilerint.index(i) + 1] = girdilerint[girdilerint.index(i)-1] - girdilerint[girdilerint.index(i)+1]
            girdilerint.pop(girdilerint.index(i))
    return girdilerint[-1]


print(islemler())












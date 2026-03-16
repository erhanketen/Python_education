

def girdi_al(girdi):

    numbers = ("0","1","2","3","4","5","6","7","8","9")
    operators = ("+","-","x","^")


    girdiler = list()
    num = ""

    for i in girdi:

        if i in numbers:
            num += i

        elif i in operators:
            if num != "":
                try:
                    girdiler.append(int(num))
                    num = ""
                    girdiler.append(i)

                except ValueError:
                    return "NotIntegerError"
            else:
                girdiler.append(i)

    if num != "":
        try:
            girdiler.append(int(num))
        except ValueError:
            return "NotIntegerError"


    return girdiler

girdi = input("Girdi:")


def indexle(girdiler):

    operator = ("x","^")
    sembol = ("+","-")

    yigin= []
    cikti = []
    op = ""

    for i in girdiler:

        if i in sembol:
            if op == "x":
                yigin.append(op)
                op = ""
            yigin.append(i)

        elif i in operator:
            op += i

        elif type(i) == int:
            if op == "x^":
                i = str(i)
                op += i
                yigin.append(op)
                op = ""
            else:
                cikti.append(i)
    if op != "":
        yigin.append(op)

    print(cikti)
    print(yigin)

    denklem = []

    while yigin:
        i = yigin.pop()
        if i == "-":
            if cikti:
                sayi = cikti.pop() * -1
                denklem.append(sayi)
            else:
                denklem.append(-1)
        elif i == "+" and cikti:
            denklem.append(cikti.pop())
        elif i == "x":
            denklem.append(i)
        elif i == "x^2":
            denklem.append(i)

    while cikti:
        denklem.append(cikti.pop())

    print(denklem)
    return denklem[::-1]


def kok_bul(denklem):

    yigin = []

    for i in denklem:
        if type(i) == int:
            yigin.append(i)
        elif i == "x^2":
            if yigin:
                a = yigin.pop()
            else:
                a = 1
        elif i == "x":
            b = yigin.pop()

    if yigin:
        c = yigin.pop()
    else:
        c = 0

    print("a:",a)
    print("b:",b)
    print("c:",c)

    delta = (b**2) - (4*a*c)

    kok1 = (-b+(delta**0.5))/(2*a)
    kok2 = (-b-(delta**0.5))/(2*a)

    return [kok1,kok2]


print(kok_bul(indexle(girdi_al(girdi))))
















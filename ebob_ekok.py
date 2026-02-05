print("************************************\n\n"
      "         EBOB-EKOK HESAPLAMA\n\n"
      "************************************")

def bolen(x):
    bolenler = [x]
    for i in range(1,x):
        if x % i == 0:
            bolenler.append(i)
    bolenler.sort()
    return bolenler



def EBOB(x,y):
    a = bolen(x)
    b = bolen(y)
    for i in a:












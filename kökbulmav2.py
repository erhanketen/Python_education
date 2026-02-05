# x^2 + 5x + 6 = 0 denkleminin köklerini bulmaya çalışalım
# -x^2 - 5x - 6 = 0
# x1 = -3 x2 = -2 olur
# a = 1 b = 5 ve c =6 olduğundan programa denkelim a b ve csini bulmasını sağlamamız gerek
print("-Kök Bulma Programı-")

denklem = input("Lütfen Denklemi Giriniz:")

# kullanıcıdan aldığımız denlemde a, b ve c'yi tanımlamamız gerekir:

print("Hesaplanıyor....")

ast = list(denklem)


if len(ast) == 8:
    if ast[0] == "x" or ast[0] =="X":
        a = 1
    else:
        a = int(ast[0])
    b = int(ast[4])
    c = int(ast[7])
    if ast[3] == "-":
        b= -b
    if ast[6] == "-":
        c = -c
elif len(ast) == 9:
    if ast[0] == "-":
        a = -1
    elif ast[1] == "x" or ast[1]=="X" and not ast[0] == "-":
        a = int(ast[0])
    b = int(ast[5])
    c = int(ast[8])
    if ast[4] == "-":
        b = -b
    if ast[7] == "-":
        c = -c
elif len(ast) == 10:
    a = - int(ast[1])
    b = int(ast[6])
    c = int(ast[9])
    if ast[5] == "-":
        b = -b
    if ast[8] == "-":
        c = -c


delta = b**2 - 4*a*c
if delta > 0 :
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
elif delta < 0 :
    print("Denklemin reel sayı kökü yoktur..")
elif delta == 0 :
    x1 = -b/(2*a)
    x2 = -b/(2*a)
print("Denklemin Birinci Kökü: {}\nDenklemin İkinci Kökü: {}".format(x1,x2))











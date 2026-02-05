print("-Kök Bulma Programı-")
# -4x^2+3x+4 / -x^2+3x-4 / x^2+x / x^2


alis = input("Denklemi Giriniz:")
denk = list(alis)

for i in denk:
    if i == "x":
        if denk[denk.index("x")+1] == "^":
            if denk[denk.index("x")-1] == "-":
                a = -1
            elif denk.index("x") == 0:
                a = 1
            else:
                a = int(denk[denk.index("x")-1])
        elif denk[denk.index("x")+1] != "^":
            if denk[denk.index("x")-1] == "+":
                b = 1
            elif denk[denk.index("x")-1] == "-":
                b = -1
            elif denk[denk.index("x")-1] != "-" or denk[denk.index("x")+1] != "^":
                if denk[denk.index("x")-2] == "+":
                    b = int(denk[denk.index("x")-1])
                else:
                    b = int(denk[denk.index("x")-1]) * -1
            else:
                b = 0


print(a)
print(b)



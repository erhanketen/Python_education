"""
Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
"""

def harf(string):

    küme = list()

    for i in string.lower() :
        küme.append(i)

    kac_tane = dict()
    küme.sort()

    for i in küme:
        if i in kac_tane:
            kac_tane[i] += 1
        else:
            kac_tane[i] = 1


    for i in kac_tane:
        print("{} harfinden {} tane var.".format(i, kac_tane[i]))

harf("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb")


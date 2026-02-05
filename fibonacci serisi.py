print("*********************************************"
      
      
      "FİBONACCİ SERİSİ"
      
      
      "*********************************************")

a = 1
b = 1
liste = [a,b]
for i in range(1,20):
    a,b = b,a+b
    liste.append(b)
print(liste)




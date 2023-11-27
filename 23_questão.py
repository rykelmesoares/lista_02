p= input('telefonou pra vitima? Responda s ou n:  ')
classificação= 0
if  p== 's':
    classificação = + 1
p= input('Esteve no local do crime? Responda s ou n: ')
if p=='s':
    classificação +=1
p= input('Mora perto da vitima?Responda s ou n: ')
if p=='s':
    classificação  +=1
p= input('Devia para a vitima? Responda s s ou n: ')
if p=='s':
    classificação +=1
p= input('Já trabalhou com a vitima?Responda s ou n:  ')
if p=='s':
    classificação  +=1
if classificação < 2:
    print("Inocente")
elif classificação == 2:
    print("Suspeita")
elif classificação < 5:
    print("Cúmplice")
else:
    print("Assassino")
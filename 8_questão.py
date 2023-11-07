p1 = float(input("digite o primeiro preço do produto"))
p2 = float(input("digite o segundo preço do produto"))
p3 = float(input("digite o terceiro preço do produto"))
if p1<p2 and p1<p3:
    print ("o primeiro produto tem um melhor  preço  sendo ", p1)
elif p2<p1 and p2<p3:
    print("o segundo produto tem um melhor preço sendo",p2)
else :
    print("o terceiro produto tem um melhor preço sendo",p3)
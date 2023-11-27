l= float(input('Digite a quantidade de litros que quer abastecer: '))
c= input('Digite qual combustivel, A para alcool ou G para gasolina: ')
preco=0
if c =='A' or c=='a':
    preco= l* 1.9
    if preco <= 20:
        preco=  l* 1.9*0.03
    else:
        preco=  l* 1.9*0.05
elif c=='G' or c=='g':
        preco=l*2.5
        if preco <=20:
            preco= l* 1.9*0.04
        else:
            preco= l* 1.9*0.06
print('O valor a ser pago é'.format(preco))
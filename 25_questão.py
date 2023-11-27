morango=float(input('Digite a quantidade em kg de morango: '))
maca=float(input('Digite a quantidade em kg de maçã: '))
if morango<=5:
    valor= morango*2.5
else:
    valor = morango*2.2
if maca<=5:
    valor= maca*1.8
else:
    valor=maca*1.5
if (morango+maca)>8 or valor>25:
    valor= valor*0.10
print('O preço a ser pago é {}'.format(valor))
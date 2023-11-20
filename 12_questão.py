vh = float(input("Digite quanto você recebe por hora: "))
ht = float(
    input("Digite quantas horas você trabalhou esse mês: ")
)
sb= vh * ht
if sb <= 900:
    desconto_ir = 0.0
elif sb <= 1500:
    desconto_ir = 5
elif sb <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

IR = sb * (desconto_ir / 100)
INSS = sb * (10 / 100)
FGTS = sb * (11 / 100)
td= IR + INSS
sl = sb - td

print(
    f"\nSalário Bruto     : R${sb:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${td:.2f}",
    f"\nSalário Liquido   : R${sl:.2f}",
)
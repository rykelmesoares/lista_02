dint = int(input("Digite o número do dia da semana (1-7): "))
dstr = ""
if dint == 1:
    dstr = "Domingo"
elif dint == 2:
    dstr = "Segunda"
elif dint == 3:
    dstr = "Terça"
elif dint == 4:
    dstr = "Quarta"
elif dint == 5:
    dstr = "Quinta"
elif dint == 6:
    dstr = "Sexta"
elif dint == 7:
    dstr = "Sábado"
if dstr == "":
    print("Valor inválido")
else:
    print("O dia correspondente é ",dstr)
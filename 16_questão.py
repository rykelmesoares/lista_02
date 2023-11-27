dia= int(input('Digite o dia: '))
mes= int(input('Digite o mês'))
ano=int(input('Digite o ano'))
if dia<1 or dia >31:
    print('dia inválido')
elif mes<1 or mes>12:
     print('mes inválido ') 
elif ano<0:
    print('Ano inválido')
else:
    print('Data válida')
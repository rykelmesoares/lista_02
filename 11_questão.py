sa= float(input("Digite seu salário atual kkk pobre: "))
sat = 0.0
dt = 0.0
pa = 0.0
if sa <= 280:
    pa = 20
elif sa<= 750:
    pa = 15
elif sa<= 1500:
    pa = 10
else:
    pa = 5
dt = sa * (pa / 100)
sat = sa + dt
print("Seu salário antes do reajuste era de R$",sa)
print("Seu salário foi aumentado em ",pa)
print("Seu salário foi aumentado em R$",dt)
print("Seu salário atual é de R$",sat)
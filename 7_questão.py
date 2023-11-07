n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))
if n1>n2>n3 or n1>n3>n2:
    print("O maior número é: ", n1)
elif n2>n3>n1 or n2>n1>n3:
    print("O maior número é: ", n2)
elif n3>n2>n1 or n3>n1>n2:
    print("O maior número é: ", n3)
if n1<n2<n3 or n1<n3<n2:
    print("O menor número é: ", n1)
elif n2<n3<n1 or n2<n1<n3:
    print("O menor número é: ", n2)
elif n3<n2<n1 or n3<n1<n2:
    print("O menor número é: ", n3)
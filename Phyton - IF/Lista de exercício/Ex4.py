n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número: "))

if n1 == n2:
    resultado = n1 * n2
    print(f"A multiplicação entre os dois números é {resultado}")
elif n1 > n2:
    resultado = n1 - n2
    print(f"A subtração entre os dois números é {resultado}")
else:
    resultado = n1 + n2
    print(f"A soma dos dois é {resultado}")
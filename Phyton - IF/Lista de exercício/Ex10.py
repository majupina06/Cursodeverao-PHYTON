num1 = float(input("Digite o primeiro número (menor): "))
num2 = float(input("Digite o segundo número (médio): "))
num3 = float(input("Digite o terceiro número (maior): "))


num4 = float(input("Digite o quarto número: "))

if num4 >= num3:
    ordem = [num4, num3, num2, num1]
elif num4 >= num2:
    ordem = [num3, num4, num2, num1]
elif num4 >= num1:
    ordem = [num3, num2, num4, num1]
else:
    ordem = [num3, num2, num1, num4]


print("Números em ordem não-crescente:")
for numero in ordem:
    print(numero)

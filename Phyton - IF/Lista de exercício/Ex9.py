num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        ordem = [num1, num2, num3]
    else:
        ordem = [num1, num3, num2]
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        ordem = [num2, num1, num3]
    else:
        ordem = [num2, num3, num1]
else:
    if num1 <= num2:
        ordem = [num3, num1, num2]
    else:
        ordem = [num3, num2, num1]


print("Números em ordem crescente:")
for numero in ordem:
    print(numero)
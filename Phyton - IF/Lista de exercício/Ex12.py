import math 
print("Menu de opções:")
print("1. Somar dois números")
print("2. Raiz quadrada de um número")

opcao = int(input("Escolha uma opção (1 ou 2): "))


if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é {soma}.")
elif opcao == 2:
    num = float(input("Digite um número para calcular a raiz quadrada: "))
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz:.2f}.")
else:
    print("Opção inválida.")

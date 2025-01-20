numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(f"Analisando o número {numero}")
    if numero == 5:
        print("Número encontrado")
        break
    print(f"Numero {numero} não é 5")

print("Loop encerrado")
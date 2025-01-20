numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    n = int(input("Digite o valor do número"))
    print(f"Analisando o número {numero}")
    if n == 5:
        print("Número 5 encontrado")
        break
    print(f"Numero {n} não é 5")

print("Loop encerrado")
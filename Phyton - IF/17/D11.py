ano_atual = int(input("Digite o ano atual: "))
salario = 1000
porc = 1.5/100
salario_novo = salario + salario * porc

for i in range (2017,ano_atual + 1):
    porc = 2 * porc
    salario_novo = salario_novo + porc

print("O salário atual é: ", salario_novo)
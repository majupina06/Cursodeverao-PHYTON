salario = float(input("Digite seu salário: "))
porc = float(input("Digite a porcentagem: "))

poc = (salario * porc) / 100
total = poc + salario


print(f"Esse é o total do seu salário: \n", total)
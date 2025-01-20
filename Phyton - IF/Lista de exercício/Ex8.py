nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")


if media < 3.0:
    print("Situação: Reprovado")
elif 3.0 <= media < 7.0:
    print("Situação: Exame Final")
 
    nota_exame = (6.0 * 2) - media
    print(f"Nota necessária no exame para aprovação: {nota_exame:.2f}")
else:
    print("Situação: Aprovado")

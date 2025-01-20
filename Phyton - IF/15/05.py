nome = str(input("Informe seu nome:"))
idade = float(input("Informe sua idade: "))

if idade >= 18:
    print(f"{nome} tem permissão para tirar carteira de motorista")
else:
    print(f"{nome} não está apto a tirar carteira de motorissta, pois sua idade é {idade}")
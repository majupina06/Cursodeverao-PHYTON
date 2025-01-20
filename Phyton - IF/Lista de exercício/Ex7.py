nn = int(input("Possui nome negativado?: "))
if nn == 0:
    print(f"Você passou para a próxima fase!")
else:
    print(f"Você foi reprovado.")

ct = int(input("Possui carteira assinada?: "))
if ct == 1:
    print(f"Você passou para a próxima fase!")
else:
    print(f"Você foi reprovado.")

cp = int(input("Possui casa própria?: "))
if cp == 1:
    print(f"Você conseguiu o empréstimo!")
else:
    print(f"Você foi reprovado.")
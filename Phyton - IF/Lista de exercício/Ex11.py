import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c
print(f"Delta: {delta}")

if delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Uma raiz real: {raiz:.2f}")
else:
    print("A equação não possui raízes reais.")
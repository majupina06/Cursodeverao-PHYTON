N = int(input("Digite um número: "))

f = 1
for i in range(N, 1, -1):
    f = f * i
    print(i)
print(f)


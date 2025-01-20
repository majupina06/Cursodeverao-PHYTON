cont = 0
while True:
    num = int(input("Insira um número"))
    if num == 0:
        break
    if num > 0:
        cont += 1
print("QUantidade de valores positivos",cont )
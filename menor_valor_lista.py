def imprimir_menor(num1, num2, num3, num4):
    inteiro = [num1, num2, num3, num4]
    menor = inteiro[0]
    for i in inteiro:
        if i<menor:
            menor = i
    return menor

num1 = int(input("numero 1:"))
num2 = int(input("numero 2:"))
num3 = int(input("numero 3:"))
num4 = int(input("numero 4:"))
menor = imprimir_menor(num1, num2, num3, num4)
print(menor)

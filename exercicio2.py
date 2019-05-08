import random  

def descobrir_menor_inteiro(num1, num2, num3):
    inteiro = [num1, num2, num3]
    menor = inteiro[0]
    for  i in inteiro:
        if i < menor:
            menor = i
    return menor


def verificar_tipo_triangulo(valor_x, valor_y, valor_z):
    if valor_x > valor_y + valor_z or valor_y > valor_x + valor_z or valor_z > valor_y + valor_x:
        return "Não é um triângulo"

    if valor_x == valor_y and valor_x == valor_z:
        return "Triângulo Equilátero"

    if valor_x == valor_y or valor_x == valor_z or valor_y == valor_z: 
        return "Triângulo Isósceles"

    if valor_x != valor_y and valor_x != valor_z and valor_y != valor_z:
        return "Triângulo Escaleno"


def calcular_media(prova1, prova2, prova3):

    if prova1.lower() and prova2.lower() and prova3.lower() == "faltei":
        media = 0

    if prova1.lower() and prova2.lower() == "faltei":
        media  = prova3/3
    if prova1.lower() and prova3.lower() == "faltei":
        media  = prova2/3
    if prova3.lower() and prova2.lower() == "faltei":
        media  = prova1/3

    if prova1.lower() == "faltei":
        media  = prova2 + prova3/3
    if prova2.lower() == "faltei":
        media  = prova1 + prova3/3
    if prova3.lower() == "faltei":
        media  = prova2 + prova1/3

    soma  = prova1 + prova2 + prova3
    media = soma/3


    if media < 3:
        return "Reprovado", media

    if media >=7:
        return"Aprovado", media 

    if media <7 and media >=3:
        return "Em recuperação", media


def imprimir_figura(numero):
  lista_de_numero = []
  for linha in range (1,numero+1):
    lista_de_numero.append(linha * "*")
  return lista_de_numero

def calcular_par_impar(numero):
    if numero%2 == 0:
        return "Par"
    if numero%2 != 0:
        return "Ímpar"

    
"""FALTA A SEIS"""


def adivinhar_valor(numero):
    valor = random.randint(1,1510)
    if numero == valor:
        return "Acertou"

    if numero > valor:
        return "O valor é menor, tente outra vez"

    if numero < valor:
        return "O valor é maior, tente outra vez"


"""FALTA A OITO"""


def ordenar_valores(valores):
    ordenar = valores
    numeros_ordenados = sorted(ordenar)
    return numeros_ordenados
    
 """FALTA A DEZ """
   
if __name__=="__main__":

    print("Opções de funções")
    print("1-Determinar o menor dos inteiros")
    print("2- Verificar tipo do triângulo")
    print("3- Média de três notas")
    print("4- Verificar par ou ímpar")
    print("5- Imprimir figura")
    print("6- Calcular expressão")
    print("7- Jogo de adivinhar o número")
    print("8- Ordenar valores")
    print("9- Números em ordem crescente")
    print("10- Procurar informação na lista ")

    opcao = int(input("Insira a opção: "))

    if opcao == 1:

        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        num3 = float(input("Número 3: "))
        menor_int = descobrir_menor_inteiro(num1, num2, num3)
        print(menor)


    if opcao == 2 :

        valor_x = float(input("Valor de X: "))
        valor_y = float(input("Valor de Y: "))
        valor_z = float(input("Valor de Z: "))
        triangulo = verificar_tipo_triangulo(valor_x, valor_y, valor_z)       
        print(triangulo)


    if opcao == 3: 

        prova1 = float(input("Nota prova 1: "))
        prova2 = float(input("Nota prova 2: "))
        prova3 = float(input("Nota prova 3: "))
        nota = calcular_media(prova1, prova2, prova3)
        print(nota)


    if opcao == 4: 

        numero  = float(input("Número de linhas: "))
        triangulo = imprimir_figura(numero)
        print(triangulo)


    if opcao == 5:

        numero  = input("Valor para descobrir se é ímpar ou par: ")
        valor = calcular_par_impar(numero)
        print(valor)


    if opcao == 6:

        print("Em manutenção")


    if opcao == 7:

        numero  = input("Valor para tentar adivinhar: ")
        adivinhar = adivinhar_valor(numero)
        print(adivinhar)


    if opcao == 8:

        print("Em manutenção")

    if opcao == 9: 

        valores = float(input("Entre com os valores que irão ser ordenados: "))
        ordenar = ordenar_valores(valores)
        print(ordenar)


    if opcao == 10:

        print("Em manutenção")

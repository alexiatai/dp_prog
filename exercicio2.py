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


def criar_triangulo(numero):
  lista_de_numero = []
  if numero <= 0 :
    exit("Insira um nº maior que zero")
  for linha in range(1, numero+1):
    lista_de_numero.append("*" *linha)
  return lista_de_numero
  
numero = int(input("Insira o nº de linhas: "))
lista = criar_triangulo(numero)

def calcular_par_impar(numero):
    if numero%2 == 0:
        return "Par"
    if numero%2 != 0:
        return "Ímpar"

    
"""FALTA A SEIS"""

def imprimir_figura(numero):
  lista_de_numero = []
  for linha in range (1,numero+1):
    lista_de_numero.append(linha * "*")
  return lista_de_numero
  
numero = int(input("Insira as linhas: "))
lista = imprimir_figura(numero)
for linha in lista:
  print(linha)



def adivinhar_valor(numero):
    valor = random.randint(1,1510)
    if numero == valor:
        return "Acertou"

    if numero > valor:
        return "O valor é menor, tente outra vez"

    if numero < valor:
        return "O valor é maior, tente outra vez"

def ordenar_valores(valores):
    ordenar = valores
    numeros_ordenados = sorted(ordenar)
    return numeros_ordenados
    
 """FALTA A DEZ """
   

if __name__=="__main__":

    print("Opções de funções")
    print("1- Receber 3 inteiros e devolver o menor deles.")
    print("2- Verificar se  ́e um triângulo equilátero, isóceles ou escaleno.")
    print("3- Situação e média de um  aluno.")
    print("4- Calcular gasto de gasolina")
    print("5- Imprimir nome e qte de letras")
    print("6- Calcular salário do vendedor")
    print("7- Trocar valor de variáveis")
    print("8- Equação do segundo grau")
    print("9- Converter graus em fahrenheit")
    print("10- Média ponderada")

opcao = int(input("Insira a opção: "))

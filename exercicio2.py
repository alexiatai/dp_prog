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

    if prova1.lower() and prova2.lower() prova3.lower() == "faltei":
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

    if soma  = prova1 + prova2 + prova3
        media = soma/3


    if media < 3:
        return "Reprovado", media

    if media >=7:
        return"Aprovado", media 

    if media <7 and >=3:
        return "Em recuperação", media



"""Fa ̧ca um programa que dadas as notas P1, P2 e P3 de um aluno de computa ̧c ̃ao 1, informe a situa ̧c ̃ao e
m ́edia deste aluno. Caso o aluno tenha faltado a alguma prova, a entrada deve ser dada como “faltei”."""

def criar_triangulo(numero):
  lista_de_numero = []
  if numero <= 0 :
    exit("Insira um nº maior que zero")
  for linha in range(1, numero+1):
    lista_de_numero.append("*" *linha)
  return lista_de_numero
  
numero = int(input("Insira o nº de linhas: "))
lista = criar_triangulo(numero)


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

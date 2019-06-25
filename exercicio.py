
   
def calcular_area(base, altura):
   if base < 0 or altura < 0:
      return "nan"
    return (base*altura)/2


def calcular_perimetro(ladoA, ladoB, ladoC):
        return ladoA+ladoB+ladoC


def calcular_almoco(valor_suco, valor_prato, valor_sobremesa):
    soma  = valor_prato+valor_sobremesa+valor_suco
    acrescimo = soma*0.10
    total = soma+acrescimo
    return total


def calcular_qte_gasolina(dist_total):
    km = 12
    qte_gasolina = dist_total/km
    return qte_gasolina


def ler_nome(nome):
    contar = len(nome)
    return contar


def calcular_salario(numero_carros_vendidos, valor_vendas, salario_fixo, comissao_carro_vendido):
    comissao_total_carros_vendidos = numero_carros_vendidos*comissao_carro_vendido
    comissao_vendas = valor_vendas*0.05
    salario_total = salario_fixo + comissao_total_carros_vendidos + comissao_vendas 
    return salario_total
    

def trocar_variavel(a,b):
    novo_a =  b
    novo_b = a
    return novo_a, novo_b


def calcular_equacao(valor_x, valor_a, valor_b, valor_c):
    equacao = valor_a * (valor_x**2) + valor_b * valor_x + valor_c 
    return equacao


def converter_celsius_fahrenheit(celsius):
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit

    
def calcular_media(nota1, nota2, nota3):
    media = (nota1*2) + (nota2*3) + (nota3*5)
    ponderada = media/(2+3+5)
    return ponderada 

if __name__=="__main__":

    print("Opções de funções")
    print("1- Calcular área do triângulo")
    print("2- Calcular perímetro do triângulo")
    print("3- Calcular o valor da conta")
    print("4- Calcular gasto de gasolina")
    print("5- Imprimir nome e qte de letras")
    print("6- Calcular salário do vendedor")
    print("7- Trocar valor de variáveis")
    print("8- Equação do segundo grau")
    print("9- Converter graus em fahrenheit")
    print("10- Média ponderada")

    opcao = int(input("Insira a opção: "))

    if opcao == 1:

        base = float(input("Base: "))
        altura = float(input("Altura: "))
        area = calcular_area(base, altura)
        print(area)


    if opcao == 2 :

        ladoA = float(input("Lado A: "))
        ladoB = float(input("Lado B: "))
        ladoC = float(input("Lado C: "))
        perimetro = calcular_perimetro(ladoA, ladoB, ladoC)
        print(perimetro)


    if opcao == 3: 

        valor_suco = float(input("Valor do suco: "))
        valor_prato = float(input("Valor do prato principal: "))
        valor_sobremesa = float(input("Valor sobremesa: "))
        almoco = calcular_almoco(valor_suco, valor_prato, valor_sobremesa)
        print(almoco)


    if opcao == 4: 

        dist_total  = float(input("Distância total: "))
        qte_gasolina = calcular_qte_gasolina(dist_total)
        print(qte_gasolina)


    if opcao == 5:

        nome  = input("Nome: ")
        ler_nome = ler_nome(nome)
        print(ler_nome)


    if opcao == 6:

        numero_carros_vendidos = int(input("Número de carros vendidos: "))
        valor_vendas = float(input("Valor vendas: "))
        salario_fixo = float(input("Valor salário fixo: "))
        comissao_carro_vendido = float(input("Comissão por carro vendido: "))
        salario = calcular_salario(numero_carros_vendidos, valor_vendas, salario_fixo, comissao_carro_vendido)
        print(salario)


    if opcao == 7:

        a = input("Valor de A: ")
        b = input("Vaor de B: ")
        trocar_variavel = trocar_variavel(a,b)
        print(trocar_variavel)


    if opcao == 8:

        valor_x = float(input("Valor de x: "))
        valor_a = float(input("Valor de a: "))
        valor_b = float(input("Valor de b: "))
        valor_c = float(input("Valor de c: "))
        equacao = calcular_equacao(valor_x, valor_a, valor_b, valor_c)
        print(equacao)


    if opcao == 9: 

        celsius = float(input("Celsius: "))
        converter = converter_celsius_fahrenheit(celsius)
        print(converter)


    if opcao == 10:


        nota1 = float(input("Nota1: "))
        nota2 = float(input("Nota2: "))
        nota3 = float(input("Nota3: "))
        media  = calcular_media(nota1, nota2, nota3)
        print(media)
        


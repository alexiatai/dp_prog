print("Entre com a opção de sua preferência")
opcao = int(input("1- Exercício 1, 2- Exercício 2, 3- Exercício 3, 4- Exercício 4, 5- Exercício 5, 6- Exercício 6, 7- Exercício 7, 8- Exercício 8, 9- Exercício 9, 10- Exercício 10"))
if opcao == 1:
    
    def calcular_area(base, altura):
        return (base*altura)/2

if opcao == 2:

    def calcular_perimetro(ladoA, ladoB, ladoC):
        return ladoA+ladoB+ladoC

if opcao == 3:

    def calcular_almoco(valor_suco, valor_prato, valor_sobremesa):
        soma  = valor_prato+valor_sobremesa+valor_suco
        acrescimo = soma*0.10
        total = soma+acrescimo
        return total

if opcao == 4:

    def calcular_qte_gasolina(dist_total):
        km = 12
        qte_gasolina = dist_total/km
        return qte_gasolina

if opcao == 5:

    def ler_nome(nome):
        contar = len(nome)
        return nome, contar

if opcao == 6:

    def calcular_salario(numero_carros_vendidos, valor_vendas, salario_fixo, comissao_carro_vendido):
        comissao_total_carros_vendidos = numero_carros_vendidos*comissao_carro_vendido
        comissao_vendas = valor_vendas*0.05
        salario_total = salario_fixo + comissao_total_carros_vendidos + comissao_vendas 
        return salario_total
    
 if opcao == 7:
    
  def trocar_variavel(a,b):
  novo_a =  b
  novo_b = a
  return novo_a, novo_b

if opcao == 9: 

    def converter_celsius_fahrenheit(celsius):

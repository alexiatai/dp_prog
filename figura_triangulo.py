def criar_triangulo(numero):
  lista_de_linhas = []
  if numero <=0:
    exit("Insira um nº maior que ZERO")
  for linha in range (1,numero+1):
    lista_de_linhas.append(linha * "*")
  return lista_de_linhas
  
numero = int(input("Insira o nº de linhas: "))
lista = criar_triangulo(numero)
lista = lista[::-1]
for linha in lista:
  print(linha)

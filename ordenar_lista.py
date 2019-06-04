def ordenar_listas(lista):
    for pivo in range(len(lista)-1):
        for teste in range(pivo+1, len(lista)):
            if lista[pivo] > lista[teste]:
                return lista
  
lista = int(input("numeros:"))
ordenar = ordenar_listas(lista)
print(ordenar)

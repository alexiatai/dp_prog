class Estado:

    def __init__(self, nome, capital, dimensao, lista_cidades, lista_estados_fronteira):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.lista_cidades = []
        self.lista_estados_fronteira = []
    
    def definir_instancias(self, nome, capital, dimensao): 
        nome = "Santa Catarina"
        capital = "Floripa"
        dimensao = "x"

    def verificar_estado_igual(self, nome, capital, lista_cidades):
        for cidade in lista_cidades:
            if nome == nome and capital == capital and cidade == cidade:
                return "Estados iguais"
            else:
                return "Estados diferentes"

nome = input("Entre com o nome do estado: ")
capital = input("Entre com a capital do estado: ")
dimensao = float(input("Entre com a dimensao do estado: "))
lista_cidades = list(input("LIsta de cidades do estado: "))
lista_estados_fronteira = list(input("Lista de cidadas que fazem fronteira com o estado escolhido: "))

verificar = Estado.verificar_estado_igual(nome, capital, lista_cidades)
print(verificar)
    

class Estado:

    def __init__(self, nome, capital, dimensao):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.lista_cidades = []
        self.lista_estados_fronteira = []
    
    def verificar_estado_igual(self, nome, novo_estado):
        if self.nome == novo_estado.nome:
            if self.capital == novo_estado.capital:
                for cidade in self.lista_cidades:
                    if cidade not in novo_estado.lista_cidade:
                        return False
                    return True
                return False
            
    def virificar_fronteira(self, estado):>
        if self.verificar_estado(estado) is False:
            self.lista_fronteira.append(estado)
            return True
        return False
            
    def 

nome = input("Entre com o nome do estado: ")
capital = input("Entre com a capital do estado: ")
dimensao = float(input("Entre com a dimensao do estado: "))
lista_cidades = list(input("LIsta de cidades do estado: "))
lista_estados_fronteira = list(input("Lista de cidadas que fazem fronteira com o estado escolhido: "))

verificar = Estado.verificar_estado_igual(nome, capital, lista_cidades)
print(verificar)
    

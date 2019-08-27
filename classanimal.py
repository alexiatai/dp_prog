class Animal:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, idade, nome, raca, cor_pelo):
        super().__init__(idade, nome)
        self.raca = raca
        self.cor_pelo = cor_pelo

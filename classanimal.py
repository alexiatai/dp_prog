class Animal:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, raca, cor_pelo):
        self.raca = raca
        self.cor_pelo = cor_pelo
